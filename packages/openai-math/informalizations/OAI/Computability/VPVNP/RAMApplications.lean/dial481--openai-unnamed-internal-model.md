---
{
  "module": "OAI/Computability/VPVNP/RAMApplications.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMApplications.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMApplications.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The live and virtual applications of the RAM transcript lemma

The live processors use a private call clock `n^10000`. The processors
of the virtual RAM use `n^10`. Both inherit the same quartic word width.
The bounds below hold on every local incident vector and branch stream,
including those obtained from a tensor expansion.


### `ProcessorBudget`

 Enough word space for every record and for the physical bit addresses,
together with the numerical bounds used by the local validator clock. 

### `eventually_bothProcessorBudgets`

 One eventual threshold works for both processors' message formats and
their cutoffs in §§10–12. 

### `ProcessorBudget.validate_clock`

 Section 10's live `n^100030` bound and Section 12's virtual `n^130`
bound apply uniformly to the concrete instruction table and all local input
values at the respective lengths. 
