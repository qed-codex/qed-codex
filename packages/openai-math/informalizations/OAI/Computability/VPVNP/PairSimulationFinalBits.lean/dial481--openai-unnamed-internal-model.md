---
{
  "module": "OAI/Computability/VPVNP/PairSimulationFinalBits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationFinalBits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationFinalBits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native scan of the final arc bits

After the compression descriptors have supplied the total width, the burst
starts at the exclusive upper address of the final bit array. Each data call
decrements this cursor, makes one binary choice, writes its value at the new
cursor and returns that cursor. The lower address is fixed public data, so
the same instruction table works for every selection of compression terms.
The reads at the two incident positions use the same prefix-sum address.


### `instruction`

 The two registers hold the cursor and a temporary word. The data calls
return to the dispatcher. At the lower address the fragment jumps to its
continuation without making a choice or accessing external memory. 

### `Linked`

 The ten scan instructions occupy their designated labels in the host machine. 

### `bitReport`

 Report of one bit call. 

### `execute_bit`

 Exact native execution of a data call on *any* supplied branch stream.
Missing or unused bits reject even when the machine has excess fuel. 

### `execute_done`

 The lower-bound test composes with arbitrary native continuation code. 

### `template`

 Standalone table with an accepting continuation. The ten labels of the
scan are embedded unchanged in this eleven-instruction template. 

### `cursor`

 Ascending physical address; the scan visits the addresses in reverse. 

### `calls`

 A successful branch stream for the whole scan, before the continuation. 

### `reports`

 Exact chronological reports for the choices written in the scan. 

### `run_scan`

 The native scan can be followed by arbitrary further calls. The memory
passed to those calls is the memory obtained by replaying the actual writes. 

### `scan_complete`

 For any scan of the prescribed length, success forces one singleton
choice per physical address. This excludes all extra and missing choices. 

### `ScanPaths`

 Histories reaching the end of the data phase in exactly the scheduled
number of calls. The subsequent vertex visits supply the continuation. 

### `scanEquiv`

 Bijective enumeration by native branch paths, including the empty scan. 

### `accepted_iff`

 With an accepting exit, every complete native history consists of the
data choices followed by the deterministic halt call. Here the stream is
unrestricted: reaching acceptance itself forces the number of data calls. 

### `scan_cost`

 Exactly one call and one external write per physical bit. 

### `readback`

 The physical cell at every address receives the unique bit chosen there. 

### `outside`

 All cells outside the scanned interval retain their previous contents. 

### `index`

 Edge number and offset address a single contiguous bit array. 

### `arcWords`

 Splitting the scan into its arc words, including the unique empty word
for every zero-width arc. 

### `payloads`

 A scan assignment is precisely a payload assignment to the edges of the
network in the contraction formula. Parallel arcs keep distinct numbers. 

### `endpoint_bits`

 Both incident payloads in equation (7.1) read the stored bit, even for
loops or multiple edges with identical endpoints. 

### `execute_endpoint_read`

 The two reads may belong to different vertex calls. From either read
label the interpreter passes precisely the incident value to its private
destination register, preserves external memory and consumes no choice. 

### `networkScanEquiv`

 For the actual fixed template, the independent summation indices of the
network biject onto the native scan histories. 

### `acceptedNetworkEquiv`

 Complete accepting paths of the standalone table enumerate each network
summand exactly once, with no restriction on the proposed history length. 
