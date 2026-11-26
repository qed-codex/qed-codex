---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorSiteTests.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorSiteTests.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorSiteTests.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Entry, call dispatch, and final checks for a RAM processor

A running entry must start inside its own half-open cost bucket. A halted
entry is checked only against the global cap. Later calls may cross the bucket
boundary, including when a final cost equals the global cap. The final
comparison distinguishes an absent outgoing edge from a present halted cut.


### `Snapshot.cut`

 Decode the current cut from the cumulative cost and, while running, the persistent state
word. 

### `Snapshot.target`

 Decode the optional outgoing cut using the presence and running flags, target cost and
target state. 

### `entry`

 Check the incoming range and choose the first site action. 

### `iteration`

 Test the cut produced by the preceding charged call. 

### `finalCheck`

 Exact use of choices and equality with the successor cut, or acceptance
at the terminal site. The state payload of a halt is ignored. 

### `final_eq_finishReports`

 A terminal equality test of the physical processor has exactly the
Boolean outcome of the native report checker. 

### `runSiteLoop_at_exit`

 The dispatch label selects precisely the native call of this site,
including its remaining credit and unused binary choices. 

### `runSite_at_exit`

 The entry fragment rejects an invalid incoming bucket and immediately
finishes on a valid halted cut. Its dispatch label enters the native site loop. 
