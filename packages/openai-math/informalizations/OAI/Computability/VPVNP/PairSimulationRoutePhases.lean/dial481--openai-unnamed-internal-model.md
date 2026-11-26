---
{
  "module": "OAI/Computability/VPVNP/PairSimulationRoutePhases.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRoutePhases.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRoutePhases.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The triangular sorting-phase traversal

The outer counter supplies the phase to the step scan. Its step bound is
phase plus one, so the offset after each phase is the start of the next
triangular layer block. Every layer's routing check enters the final mask.


### `PhaseState`

 Prefix invariant after a given number of complete sorting phases. 

### `phases_exact`

 Run all sorting fields using the same fixed phase and step control code
at every input size. The clock counts every visit on malformed inputs. 

### `phases`

 The sorting traversal is bounded by the same clock on all inputs. 
