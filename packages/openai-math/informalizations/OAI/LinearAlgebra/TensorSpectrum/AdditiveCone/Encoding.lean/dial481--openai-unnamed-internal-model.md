---
{
  "module": "OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/Encoding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/Encoding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/TensorSpectrum/AdditiveCone/Encoding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# From absence of additive states to an actual catalyst

Finite coordinate bounds and state constraints are encoded by integer vectors.
Their integer cone certificate is evaluated in the stable additive group, so
the final inequality retains the catalyst and requires no cancellation in `S`.


### `catalyst_of_no_state`

 Failure of the normalized additive monotone state space produces a genuine
strict positive integer gain with one catalyst. All finite encoding and cone
steps are proved from the given semiring and order hypotheses. 
