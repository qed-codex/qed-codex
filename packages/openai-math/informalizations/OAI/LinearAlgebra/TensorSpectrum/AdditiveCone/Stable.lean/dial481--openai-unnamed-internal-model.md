---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/Stable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/Stable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/Stable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Integer cone certificates evaluate in the actual additive group completion.
The resulting equality supplies a catalyst; no cancellation law for the
underlying semiring is imposed. 

### `stable_of_group_balance`

 Rearranging a group-completion equality gives precisely the stable equality
required by the catalytic argument. 

### `stable_certificate_of_integer_cone`

 Evaluate and combine a finite integer cone certificate.  Each row consists
of a monotonicity difference and a detection difference; either summand may be
zero. The unrestricted additive-relation coefficients disappear only because
their images have been proved to be zero in the group completion. 
