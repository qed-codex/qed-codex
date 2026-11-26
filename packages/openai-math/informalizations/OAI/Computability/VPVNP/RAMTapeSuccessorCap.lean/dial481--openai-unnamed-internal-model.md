---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorCap.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorCap.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorCap.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Comparing the successor cost with its cap

The cost and the cap arrive least-significant bit first. Subtracting the cap
with an initial borrow of one tests whether the cost is at most the cap.
Each pair of popped bits is saved and later returned to its original stack.


### `State`

 Control states for subtracting the cap with an initial borrow, restoring both operands, and
reporting whether the cost fits. 

### `code`

 The scratch ports `.tmp` and `.out` save the left and right inputs. 

### `run`

 Exactly eight stack instructions per bit and two empty pops. The final
state holds the unsigned comparison and all four stacks have their entry values. 

### `run_lift`

 A caller can use any four distinct ports. The entire caller stack bank
is restored, and the caller can use the terminal flag to select its continuation. 
