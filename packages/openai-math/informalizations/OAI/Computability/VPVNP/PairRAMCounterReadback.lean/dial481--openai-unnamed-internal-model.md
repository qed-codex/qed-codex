---
{
  "module": "OAI/Computability/VPVNP/PairRAMCounterReadback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRAMCounterReadback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRAMCounterReadback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the complete compressed pair's exponent array

The final vertex histograms use the descriptor order of the actual repeated
compressor. Adding them to the shared suffix gives the monomial exponents
in its template alphabet. The prefix holds the nominated production counts.


### `pairRAMHistogramsWithFuel`

 Per-vertex template histograms for the chosen virtual fuel, in final-site order. 

### `pairRAMHistograms`

 Per-vertex template histograms, ordered by the actual final-site descriptors. 

### `pairRAMHistogramsWithFuel_readback`

 At arbitrary fuel, the ordered visits recover both parts of the live exponent array. 

### `pairRAMHistograms_readback`

 The actual ordered visits recover both parts of the live exponent array. 

### `eventually_pairRAMHistogramsWithFuel_readback`

 For the paper's virtual dimensions, the final counter array
recovers the two histograms simultaneously for all programs, fuel choices, headers and paths. 

### `eventually_pairRAMHistograms_readback`

 For the paper's virtual dimensions and clock, the final counter array
recovers the two histograms simultaneously for all programs, headers and paths. 
