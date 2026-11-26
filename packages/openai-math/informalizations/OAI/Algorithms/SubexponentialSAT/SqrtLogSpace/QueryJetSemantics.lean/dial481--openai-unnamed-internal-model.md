---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryJetSemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryJetSemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryJetSemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact source jets and decoded native coefficient words for reconstruction.
The optional marked factor is a violation query, and all free assignments remain. 

### `specializeDense_jet_embedding`

 Specializing an embedded free-variable jet only reads the correction bits
on the image. In particular, the chosen high-coordinate correction bits cannot
change the dense value. 

### `residualValue_eval_scoped`

 Evaluation is required only at literals actually read by the selected ID.
The formal variable type may be the complement of the fixed high coordinates. 

### `residualProduct_specializeDense`

 The original canonical residual-factor product specializes to the actual
selected source expressions, with the same shared marker and Taylor cutoffs. 

### `colored_target_dense_shift`

 Summing the actual shifted colored expressions produces every retained
coefficient of the original fixed-high source target. 

### `residualJet_eval_diagonal`

 At the actual complete assignment, the stored baseline is the free-row
sum. Only low literal incidences require a source entry; high literals retain
their fixed bit. No supplied jet-evaluation service is used. 

### `residual_group_diagonal_dense`

 Diagonal specialization of the actual retained source factor product.
The premises are the physical assignment word and the actual literal scopes,
not evaluator outputs. The native lifting cutoff equals the fixed precision. 

### `colored_residual_target_dense_shift`

 The actual colored residual products, evaluated at all free assignments,
produce the shifted fixed-high target. Empty groups retain their neutral one,
and additive readout occurs after the complete group product. 

### `actualProduct_specializeDense`

 The actual arbitrary-state factor product specializes to its free-variable
source product. The native state supplies the high mask and bits directly;
no legacy assignment context or chosen raw representative is introduced. 

### `native_readout_hasJets`

 Actual native readout words supply all coefficients below J. Only the
retained additive readout is specified, after the complete group products. 
