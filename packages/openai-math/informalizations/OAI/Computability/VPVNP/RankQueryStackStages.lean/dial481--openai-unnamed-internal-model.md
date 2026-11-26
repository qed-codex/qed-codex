---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackStages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackStages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackStages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Installed Schur descriptor and child routines

The two child routines put a complete typed query in six auxiliary output
registers. They read the loop index from the live continuation frame. The
descriptor routine leaves a zero dummy index in the auxiliary bank.


### `Pending`

 The dispatch bank is ready and its six output registers encode the child query `q`. 

### `stageChild`

 Compute the selected left or right child query using the loop index in the live frame. 

### `stageDescribe`

 Compute the current query's descriptor with a zero dummy loop index. 

### `inputs_bounded`

 A single linear bit bound covers every query register and every loop
counter used by either child program. 
