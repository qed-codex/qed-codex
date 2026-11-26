---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgramFrontendInputBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgramFrontendInputBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafParametersProgramFrontendInputBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Input-only closure of the physical parameter/cache/export costs, including
the exact binary word lengths used by the subsequent offset producer. 

### `bundle`

 The offset producer receives actual exported binary B/Q/R words. Include
all three physical length caps and the numeric exponent R in one bound. 

### `uniform_bundle_polynomial`

 One pair of constants works for every measured query and every padding
of its eight binary inputs. No produced-value or produced-length premise. 

### `uniform_polynomial`

 Solver-facing uniform bound: source instruction costs plus the three
actual offset-input word-length caps and its numeric exponent. 

### `uniform_offset_polynomial`

 The exact offset-model expression used by the frontend postlude is also
bounded by the same input-only ordinary-polynomial method. 
