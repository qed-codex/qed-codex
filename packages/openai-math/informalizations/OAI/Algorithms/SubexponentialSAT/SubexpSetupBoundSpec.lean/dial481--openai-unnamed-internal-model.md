---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpSetupBoundSpec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSetupBoundSpec.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpSetupBoundSpec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Measured bounds for composition of the concrete setup phases

The predicates below retain actual executions. Polynomial coefficients and
degrees are chosen before the input size and the incoming machine state.


### `eval_wordBound`

 A fixed stack gains at most one bit per actual instruction. 

### `bounds_of_witness`

 A bounded witness bounds every execution of the same fixed command. 

### `PolynomialRun`

 The initial bound is a real bound on every stored word, not a declaration
that the eventual execution already has polynomial cost. 

### `PolynomialRun.of_envelope`

 Substitute a proved polynomial numerical-parameter bound into a local
execution envelope. Existence and cost remain separate checked premises. 

### `PolynomialRun.seq`

 Polynomial measured executions compose with fixed coefficients and
degrees, while passing the actual intermediate state to the second phase. 
