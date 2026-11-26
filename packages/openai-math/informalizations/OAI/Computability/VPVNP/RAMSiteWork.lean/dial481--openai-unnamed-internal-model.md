---
{
  "module": "OAI/Computability/VPVNP/RAMSiteWork.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSiteWork.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSiteWork.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Work of the bucket's private call loop

The metered loop follows the same calls as `runSiteLoop`. It reserves a fixed
control charge on each visit, including the final check, and counts dispatches,
charged probes and reserved guess slots for each attempted call. On success it
uses the accumulated probe count to advance the cut in constant time.


### `MeteredSiteRun`

 Result and word-work charge for one site’s private call loop, including paths that stop
with a failed check. 

### `MeteredSiteRun.output`

 On success, the site’s call reports in order and the suffix of the private bit stream
  left for later processing. 

### `MeteredSiteRun.work`

 Total charge for loop control, instruction dispatch, external probes, and private guesses
  on the simulated path. 

### `meteredSiteLoop`

 Meter the call loop on every input. The charge `controlCharge` covers a
fixed set of loop checks and counter updates per visit. The call charge covers
the instruction dispatch, one slot per charged probe, and the individual
binary guesses. 

### `meteredSiteLoop_output_eq`

 The counters, including the constant-time cost update, preserve the exact
result of the private choice stream. 

### `siteWork_le`

 Arbitrary incoming cuts and private bit streams satisfy the same bound,
including paths that reject after partially simulating a call. 

### `countProbesWork`

 Scan each event once, counting the probes and the operations to advance
the cursor, inspect the tag and update the count. 

### `meteredAdvance`

 Compute the outgoing cost and state in one pass over the reports and their
events. Six further operations per report cover advancing the cursor, reading
the persistent state, and updating the cost. 

### `meteredValidateSite`

 The exact-use validator reserves a fixed control budget for the incoming
range test and outgoing comparisons. The cut scan starts only after exact
consumption of the private choices. 

### `meteredValidateSite_work_le`

 The work bound for the full private site validator, including incoming
format tests and the final cut scan, on arbitrary bit streams and cuts. 

### `meteredValidateSite_work_le_product`

 A single product bounding the private validator. For the application's
fuel `n^u`, the hypothesis on the bucket follows from `H ≤ 2n` and `u ≥ 1`. 
