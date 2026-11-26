---
{
  "module": "OAI/Computability/VPVNP/RAMPrivateLogRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMPrivateLogRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMPrivateLogRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Call simulation and log capacity

The list-backed machine produces the direct machine's exact report, unused
suffix, and all three counters even on rejecting inputs. Along every possible
prefix, including arbitrary read guesses, the log grows by at most one entry
per instruction. Hence the same fixed scan allowance applies on every path.


### `runLocalCall_mapState`

 Mapping every instruction continuation preserves the whole metered call. 

### `CallAction.continuesTo`

 All continuations of a dispatched instruction, before enforcing fuel,
probe caps, or correctness of the supplied read value. 

### `InstructionPrefix`

 A prefix of `n` continuing instructions, retaining every binary choice
and possible read answer. Halting and rejection have no continuations. 

### `Machine.prefix_log_capacity`

 With `n` dispatches used out of the initial fuel, the reached log and
the remaining fuel still fit in the reserved capacity. 

### `Machine.prefix_scan_work_le`

 This bound covers each private read, regardless of the supplied address
and the persistent input. The capacity depends only on the call fuel. 
