---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpCRTOuterSetup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCRTOuterSetup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCRTOuterSetup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual initialization for the outer CRT tape controller. Widths and the
binary dimension are computed by fixed programs from the retained runtime
inputs. In particular, neither a binary exponent nor a jet-width word is
provided for free. 

### `initializedStacks`

 The exact stack result of initialization. All words here are outputs of
the concrete zero-fill, unary-count, repeated-copy, and preserving-copy calls. 
