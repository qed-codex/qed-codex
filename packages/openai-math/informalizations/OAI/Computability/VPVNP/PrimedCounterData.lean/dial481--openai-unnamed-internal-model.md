---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterData.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Parameters and initial memory for the uniform coefficient counter

The public table contains dimensions, the literal prefix, the root state and
the fixed offsets used by the native program. The exterior bits and nominated
histogram are loaded from the actual initial external memory. The same code
is used for every pair and for every nomination.


### `Data`

 Parameters for counting one primed pair coefficient at the given RAM layout and grammar
state count. 

### `Data.degree`

 Degree index installed in the pending root frame of every site's parse. 

### `Data.root`

 Grammar state required at the root of every site's parse. 

### `Data.header`

 The fixed Boolean header data for the two groups, including the exterior fields. 

### `Data.nomination`

 Requested multiplicity of each terminal and binary production in the pair's aggregate
  parse histogram. 

### `base`

 Address of the assembled input rectangle and beginning of the parser's working layout,
immediately after first-pass scratch. 

### `assembly`

 Number of scheduled calls in the two input-assembly passes, one per rectangular position
per pass. 

### `labels`

 Number of dense production counters that the final comparison scans. 

### `total`

 Total number of scheduled calls for both input passes, all site parses and all histogram
comparisons. 

### `fuel`

 Private instruction allowance per call, covering input address computation and the parser's
word operations. 

### `Fits`

 All slots of the actual machine word and both work arrays used by one invocation. 

### `parserPub`

 Fourteen parser operands including scratch layout, root degree, root state and nomination
base address. 

### `pub`

 The full public operand vector combining input assembly, parsing and the absolute schedule
boundaries. 

### `machine`

 The uniform coefficient-counting instruction table instantiated at the selected word width
and public operands. 

### `nominatedWord`

 The requested count at a dense label index, encoded as one machine word. 

### `hist`

 The nominated counts as a list of machine words in the parser's dense production order. 

### `initial`

 Initial external memory with the pair header followed by its nominated histogram. 

### `input`

 The primed processor input bits for a site in either group, assembled from its fixed header
and the shared internal assignment. 

### `Nominated`

 All words in the reserved nomination region have the values prescribed by this pair's
histogram. 

### `Holds`

 Parser memory relation including the reserved nomination words. 

### `assembled_holds`

 The native input passes start the traversal with zero counters, no marks
and no pending frames, while preserving every nomination word. 
