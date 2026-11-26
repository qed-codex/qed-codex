---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpCandidateFinalize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCandidateFinalize.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCandidateFinalize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finalize a materialized candidate assignment

The complete packed array is input on stack 8. A unary width word on stack 3
selects its first `n` bits, and stack 2 contains the accumulated label-validity
bit. The remaining padding is scanned by an actual finite zero-test program.
The output assignment is on stack 1 and the combined validity bit on stack 9.


### `prefix_trace`

 The actual extraction works for any requested prefix with enough data. 
