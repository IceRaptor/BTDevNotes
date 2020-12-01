# ModTek Notes

- was writing / reading load order from a disk-cache... why? Because the order wasn't stable from run to run and thus merges would get weird if we didn't? 
- Probably to ensure nothing changed in the order that would invalidate the merge cycle, to minimize load time?

- I'm not honoring ignoreLoadFailure... should I?
	- should there be an ignoreValidation / dependencies flag?
	
- I have an (ordered) list of modDefs
-   - Send N mod defs for processing; wait until all are processed
-   - Each modDef defers until it's dependencies are loaded
-   - How to check dependencies?

- Build event in main modtek not copying all dependencies... need to fix?


## Async Loading Investigation
- 0.7.7.6 loading ~ 20-22s with a built cache

- Running a topological sort (Medallion from NuGet), then using Tasks to multi-load helps some, but not as much as expected. ~16s load with 5 simultaneous tasks. 

Reason is that Harmony patching has a sync lock on https://github.com/pardeike/Harmony/blob/master/Harmony/Public/PatchProcessor.cs which ends up in lock contention when more than 1-2 DLLs try to load at the same time. Without significant changes to Harmony 1.2 (unlikely) or changes to how the mods patch, it's unlikely to get down to the sub-10s range.

CAC and CL always require the main thread because they are doing asset bundle loads, which messes with the dependency graph. The graph depth is basically 4-6 deep, as things like CAC -> ME -> CBTBE happen. 

Even with 25 tasks there's almost no improvement, because the harmony locks end up consuming all the time. M22 provided a nofastinvoke/better locking harmony lib and we're still at ~15s so there's no much reason to fight this battle here. Just live with the 22s load time.