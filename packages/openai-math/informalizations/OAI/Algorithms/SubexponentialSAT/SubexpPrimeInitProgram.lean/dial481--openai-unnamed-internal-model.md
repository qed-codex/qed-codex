---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPrimeInitProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPrimeInitProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPrimeInitProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Concrete initialization of trial division

The candidate is preserved on stack 9. A fixed program clears its workspace,
copies the candidate, decrements the copy twice, and writes divisor 2 and a
true primality flag. Execution is total even when the candidate is below 2;
the numerical subtraction specification requires candidate at least 2.


### `initializer_execution`

 Unconditional actual execution; no candidate lower bound is needed. 

### `initializer_correct`

 The fuel has the intended natural subtraction value when the candidate
is at least two. Exact stack representations and the candidate are preserved. 
