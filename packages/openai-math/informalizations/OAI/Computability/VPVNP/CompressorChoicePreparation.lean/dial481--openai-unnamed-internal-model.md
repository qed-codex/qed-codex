---
{
  "module": "OAI/Computability/VPVNP/CompressorChoicePreparation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorChoicePreparation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorChoicePreparation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading actual demand widths and preparing a compressor term

The local demand widths are contiguous words in external memory. Starting at
their base address, a fixed call reads each width once, accumulates the cleared
quadratic energy, and computes the repetition count by native bisection. The
next call uses that count for the actual motif's outer payload choice.


### `readCoordinate`

 The weights occupy the first public positions. The last position holds the
fixed squared block scale times the common denominator of the demand masses. 

### `scan`

 Reading the fixed denominator closes the scan. 

### `demandAt`

 Recover the demand vector in the fixed order from actual machine memory. 

### `energyPrefix`

 Shared deterministic prefix for the rounded-grid and repetition procedures.
Its first register holds the quadratic energy of the actual demand words. 

### `repetitionCall`

 After reading the fixed demand motif, bisection computes its copy count. 

### `repetition_exec`

 The complete demand-to-repetition execution preserves memory, reads exactly
the demand coordinates, and consumes no branch choices. 

### `preparation_fit`

 A fixed coefficient plus four logarithmic digits per demand-width bit
covers the midpoint sums, all squared comparisons, and the fixed public table. 

### `publicWords`

 The fixed integer data stored at the public indices of the preparation program. 

### `repetitionMachine`

 Instantiate the repetition-count worker with the ordered demand weights and the supplied
repetition parameter. 

### `execute_return`

 A deterministic structured derivation gives a complete native call at
every budget covering its executed instructions and the returning halt. 

### `repetition_native`

 The first actual call returns the computed repetition word from the demand
array. Its event count is logarithmic in the largest demand width. 

### `chooseFromDemand`

 Two ordinary calls, with the repetition call's returned word and external
memory passed to the payload reader. The sole dynamic input to the first call
is the base address of the motif's demand widths. 
