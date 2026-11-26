---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapWriterClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapWriterClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapWriterClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Canonical event sequence of the map argument writer

The native writer evaluates its expressions using the six live input
words and the external memory. The events are exactly those of the same
expression list evaluated with a zeroed compiler bank, followed by the
private descriptor stores. Thus their order and contents are determined
by the inputs even when the caller's other registers and memory vary.


### `events`

 Every public record read in assignment order followed by the fixed
private-store and cursor instructions. 

### `events_readsFrom`

 Every external read in the writer's canonical trace belongs to the
region certified for its base and field expressions. 

### `events_noWrites`

 The external memory is read-only during the complete writer, including
the descriptor stores in the private memory. 

### `native_exact`

 On every caller configuration, the linked writer executes the same
canonical trace for its input words and external records. The output
descriptor and exterior memory frame refer to this very execution. 
