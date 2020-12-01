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

## RehydrateObjectFromDictionary

Looks like custom deserialization logic that avoids NewtonSoft deserialization. Hard to see the value here, beyond some custom processing for dictionaries to allow k and v to represent key/value pairs and maybe some of the type logic. 

Generates several GC pauses and string creation.

## LoadRequest

Looks like many implementations of LoadRequest<T> that are typed, these clutter up the vast majority of the class. LoadRequests *heavily* rely upon private accessors in DataManager directly, such as the heatSinkDefs field.


### ScriptBinding
Bound to "DataManager" ref by HBS.ScriptBinding. Probably to allow unity scripts to fetch resources from the datamanager?

# SimGameState

## RequestDamageManagerResources

- Invoked when loading a simGame, appears to load pretty much everything since it loads all WeaponDefs, AmmoDefs, etc. Probably gets a transitive load through ItemCollectionDef

- Most requests have allowStacking: false, except for tooltips/descriptionDefs who are true
- 