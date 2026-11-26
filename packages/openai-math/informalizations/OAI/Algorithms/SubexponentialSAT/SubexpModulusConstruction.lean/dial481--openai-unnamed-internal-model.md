---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpModulusConstruction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpModulusConstruction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpModulusConstruction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Constructing the prime-power modulus by binary multiplication

The data routine calls the existing binary `mulRun` once per iteration and
starts with the one-bit representation of one. No natural-number exponentiation
or conversion of the encoded value occurs in the data path. A single final
traced pass trims or zero-pads the output. Cost statements count the concrete
finite-alphabet BitEvent traces, not primitive-machine execution steps.


### `powerRawRun`

 Repeated binary multiplication. The fixed input is always the first
multiplicand, which keeps the raw representation length polynomial. 

### `powerRawRun_length`

 Even before normalization, output length grows only linearly in the
number of repeated multiplications. 

### `powerRawRun_cost_le`

 One common budget bounds every multiplication up to the specified limit. 

### `powerRawRun_cost`

 A quadratic polynomial in both the iteration count and input bit length. 

### `normalizeRun`

 A single pass of exactly the requested output width. Each step inspects
an input cell and writes either its bit or a padding zero. 

### `power_lt_capacity`

 The raw arithmetic value fits in the linear target width, including n=0. 

### `powerRun`

 Modulus construction followed by one traced canonical-width pass.
Only the width counter is calculated arithmetically; encoded values are
multiplied exclusively by the Boolean/list implementation. 

### `powerRun_cost`

 Every multiplication trace and the final normalization trace are included. 

### `powerRun_cost_quadratic`

 A compact uniform polynomial bound for the complete bit-event trace. 

### `bits_eq_of_length_of_value`

 Fixed-width little-endian words are determined by their numeric value. 

### `powerRun_eq_fixedBits`

 Characterization of the output, not an implementation by natural powers. 

### `modulus_eq_fixedBits`

 With the standard prime word as input, the result is exactly the modulus
word previously specified by evaluating p^μ as a natural number. 
