# Notes on DataManager


- keeps a DictionaryStore of various elements that it's loaded
- Has MaxConcurrentLoadsHeavy, MaxConcurrentLoadLight but they don't see to do much
- Exposes several IDataItemStore<string, T> which is a key-value pair that are basically dictionary refs  

A core problem is how to replace the LoadRequests when so much other code depends on them, and they are typed in such a way they aren't easy to replace. What to do with the publics of this type?
  - all of these are hidden except for the next two

- Probably have to heavily modify DependencyLoadRequest as well, since that's passed around and used in many different places
- As well as InjectedDependencyLoadRequest
- transpiles on their constructor to return a new object of a different type? But problem is they are likely created *before* harmony patches run

JsonLoadRequest.OnLoadedWithJSON invokes TryLoadDependencies after the resource has been loaded. The deeper the dependency graph, the longer to load everything as you have to consecutively keep loading and loading. 

Changing to a model where everything in a batch loading, then all dependencies loading would lead to cases where multiple mechs all request the same MLas. Unless filtering is done.

StringDataLoadRequest.Load() looks to block on FileAssets and AssetBundles. It uses Unity LoadAsync for resources though. 

Could I add a coordinator class that would take StringDataLoadRequests, create a Task to load their resources, and await? Then StringDataLoadRequests could block on adding to a ConcurrentQueue managed by the coordinator?


#### UpdateRequests

Note that updateRequests polls each loadRequest for activeLight and activeHeavy requests. Light and Heavy in this context refer to the number of requests with allowedWeight <= 10 U and <= 1000U respectively. So 'few' versus 'many' in terms of individual loads rather than actual size of the content

For each loadRequest that's processing, it then pops off an individual FileLoadRquest from that LoadRequest and calls the Load() function on it. This is where AsyncLoadRequest gets invoked, as the StringDataLoadRequest.Load() method invokes it. 



## RehydrateObjectFromDictionary

Looks like custom deserialization logic that avoids NewtonSoft deserialization. Hard to see the value here, beyond some custom processing for dictionaries to allow k and v to represent key/value pairs and maybe some of the type logic. 

Generates several GC pauses and string creation.

## LoadRequest

Looks like many implementations of LoadRequest<T> that are typed, these clutter up the vast majority of the class. LoadRequests *heavily* rely upon private accessors in DataManager directly, such as the heatSinkDefs field. 

This typing becomes useful in the GatherDependencies step, which uses the type to define what dependency types have to be loaded as well. Most types will load an icon for status effects, display, etc - while some will load a prefab (like weapons).


LoadRequest is a sub-class of LoadTracker; look at LoadRequest.ProcessRequests. For each VersionManifestEntry in the loadRequest, it creates 2 LoadTrackers
* one that directly tracks the versionManifestEntry in its loadRequests dictionary
* one it pulls from the datamanager, by asking for the 'first active loader' (aka real loader) associated with the VME

it links it's loadRequest with the backingRequest (so backingRequest has a back-ref to the 'owning' loadrequest)
it also links the VME trackingLoadRequest to it's linkedPendingRequests

it iterates through each VME, polling for isComplete. If not:

* if allowDuplicateInstantiation is set, it will increment the cache Count on the backingRequest. This seems to create a PrewarmRequest object, which increments a CacheCount variable on the request... which doesn't seem to be used anywhere?
* If the loadRequestWeight > backingRequest's allowedWeight, it will re-set the load-weight and check for dependencies. It calls GatherDependencies() on the backing loadTracker, which spawns a raft of loaders linked to the backing loader via the backingLoader's dependencyLoader. The backingLoader then sets a timeout and starts waiting for deps.

When a backingRequest is complete, the loadTracker iterates the callbacks and invokes them and marks them done. It also iterates every linkedTracker and calls CompleteLoadTracker on them too.

If the request fails, to adds it to the failedRequests dictionary. This looks to be largely used for logging load requests in embedded modtek, updating the map image, and that's about it


### ScriptBinding
Bound to "DataManager" ref by HBS.ScriptBinding. Probably to allow unity scripts to fetch resources from the datamanager?

# SimGameState

## RequestDamageManagerResources

- Invoked when loading a simGame, appears to load pretty much everything since it loads all WeaponDefs, AmmoDefs, etc. Probably gets a transitive load through ItemCollectionDef

- Most requests have allowStacking: false, except for tooltips/descriptionDefs who are true


