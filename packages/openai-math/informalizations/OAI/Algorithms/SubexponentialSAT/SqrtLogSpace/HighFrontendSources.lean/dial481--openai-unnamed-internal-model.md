---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighFrontendSources.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighFrontendSources.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighFrontendSources.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Typed source and empty-workspace relations follow from the actual trial
and accepted source stages. Changing the marked clause does not change the
immutable source words; its scope and high mask are recomputed by the frontend. 

### `trial_sources`

 The physical candidate prefix and copied history are typed as this
query's rows; no scope, layout, or evaluated query is supplied here. 

### `accepted_sources`

 The accepted stage uses the saved history literally, with no candidate
prefix and no replacement of the declared ambient count. 

### `sources_with_mark`

 Mark selection changes query semantics and hence its newly computed high
set, but leaves the five immutable source words unchanged. 

### `workspace_sources`

 The actual collector's workspace equality preserves the source words at
every marked callback boundary. 

### `scopeRows_lt`

 Every current hashed or marked scope comes from an actual source literal.
This applies uniformly to the optional mark; no precomputed scope bound is an
input to the machine. 

### `rawQuery`

 A proof-side description of precisely the native raw records and source
words. The runtime receives the existing encoded masters, not this record. 

### `castRows`

 The semantic dependent cast retains every physically encoded row word.
It changes no clause index value and introduces no runtime row traversal. 

### `rawQueryFromRows`

 Actual selected rows and marked indices keep their literal numeric bytes
when related to the serialized clause-record indexing. 

### `rawQuery_valid`

 Concrete raw records satisfy every source-side frontend validity field.
The positive ambient case is selected by the actual terminal dispatcher. 
