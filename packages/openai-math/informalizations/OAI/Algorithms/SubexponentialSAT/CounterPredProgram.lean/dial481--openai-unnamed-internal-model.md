---
{
  "module": "OAI/Algorithms/SubexponentialSAT/CounterPredProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/CounterPredProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/CounterPredProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Saturating predecessor by fixed Boolean-stack code

A preserving zero scan guards the verified borrow routine.  Zero words, including
arbitrarily padded zero representations, are retained; positive words are
decremented without increasing their length. The callback-free code is total.


### `predResult_length`

 Both branches preserve the raw representation width, even at zero. 

### `predCost_le`

 The bound includes the compiled program's final halt instruction. 

### `predResult_stacks`

 With empty incoming scratch, the counter is the only changed stack. 

### `pred_correct`

 Assembly interface exposing the changed word and unconstrained registers. 
