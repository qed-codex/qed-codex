---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpQuarticFlatMul.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpQuarticFlatMul.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpQuarticFlatMul.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Flat-record quartic multiplication by an actual fixed Boolean-stack program

Preparation, the 49-operation word-bank multiplier, packing, and cleanup are
all executed by finite instruction tables. The prime, exponent, modulus,
reduction coefficients, and operand bits are runtime data.


### `program`

 The program is independent of every arithmetic parameter. 

### `program_run`

 Complete measured execution, including every setup/copy/cleanup step. 

### `PrimitiveRunsIn`

 The actual primitive execution proposition, with the finite program kept
abstract while the dependent configuration types are checked. 
