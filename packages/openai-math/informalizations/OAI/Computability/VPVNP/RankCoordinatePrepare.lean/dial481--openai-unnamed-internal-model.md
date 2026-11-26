---
{
  "module": "OAI/Computability/VPVNP/RankCoordinatePrepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinatePrepare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinatePrepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Preparing the actual two Cramer roots from live evaluator inputs

A fixed table clones the shared templates, computes the current original row
and replacement ordinal, converts the label when required, and writes the
four varying words to the numerator. The operation mode is fixed in control.
Both modes can start from the same advised stacks.


### `sources`

 Source ports for the numerator’s replacement-row ordinal and three target inputs. Dynamic
registers five and seven supply the ordinal and monomial. The other ports supply the label
mark and operation-specific scale. 

### `machine`

 Load the root templates, compute the replacement row from the next basis ordinal and the
target monomial from the current one, and install those words with the operation’s label
mark and scale. 

### `machine_bounded`

 Complete dynamic preparation. The live ordinal words and unary label are
the only request-dependent input. The prepared roots contain the selected
replacement row and the original powered-target monomial. 
