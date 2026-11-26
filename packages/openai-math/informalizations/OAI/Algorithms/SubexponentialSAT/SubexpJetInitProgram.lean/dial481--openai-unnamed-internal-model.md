---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpJetInitProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpJetInitProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpJetInitProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Initializing the packed output jet

The input dimension is a unary word on stack 109 and the scalar word width is
the length of stack 10.  The fixed program constructs one four-word zero
coefficient on stack 104 and copies it D times to stack 102.  It preserves both
input words.  No zero array is supplied as an input certificate.


### `command_eval`

 The program builds all D zero coefficients by actual copying loops. 
