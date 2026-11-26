---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPrimeIntervalProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPrimeIntervalProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPrimeIntervalProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A concrete first-prime interval search

The candidate test is the closed binary trial-division program. The first-success
controller stores its candidate and remaining count as binary data, and returns
the first prime in the supplied interval. Endpoint construction below is also an
actual finite program on the encoded exponent.


### `intervalSearch_correct`

 No abstract callback hypothesis remains: each visited candidate invokes
the closed binary primality program. The result is exactly the first prime. 

### `endpointStack`

 Fixed endpoint ports: exponent 0, scratch 1, lower 2, start 9,
remaining count 10, upper 3. 

### `exponentSearch_correct`

 On an encoded exponent, the program computes the same strict dyadic
interval scan used by the packing schedule. 

### `writeDefault`

 Write the schedule's explicit fallback value using a clear loop and
three bit instructions. 

### `primeSelect_schedule`

 The actual program computes the schedule's total prime-selection value
from a binary encoding of its exponent, including the small-input fallback. 
