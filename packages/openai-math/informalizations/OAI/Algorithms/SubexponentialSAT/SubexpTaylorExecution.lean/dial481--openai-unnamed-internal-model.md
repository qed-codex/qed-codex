---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpTaylorExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTaylorExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpTaylorExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable Taylor and factor preprocessing for coefficient code words

Only RingProgram callbacks occur in runtime definitions. Code words need no
ring laws. Decoding the computed arrays yields the true shifted-polynomial
coefficients. Arithmetic callback costs and list visits are kept separate.


### `buildFactorProgram_taylor`

 The local semantic contract required by the represented factor builder. 

### `preparedFactors`

 Actual prepared binary callbacks instantiate the complete frontend; the
runtime arguments contain no semantic ring decoder or cost-bound certificate. 
