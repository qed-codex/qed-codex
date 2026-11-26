---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSiteCutBank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteCutBank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteCutBank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The successor guard on the actual public processor bank

The reader addresses the parsed site and incident bits, the computed word width and cap,
and the literal initial word directly in the public bank. Its running flags, decoded words
and record payloads occupy separate auxiliary stacks. The guarded output below is the exact
stack state supplied to the call loop or sorting pass on a valid pair of successor fields.


### `Aux`

 Auxiliary guard ports for outgoing presence, per-side status, endpoint records, and eight
decoded words on each side. 

### `Port`

 Combined public processor and successor-guard auxiliary bank. 

### `ports`

 Connect the successor reader to the parsed public fields and its dedicated scratch,
decoded-word, and endpoint-record ports. 

### `checked`

 Run the two successor-field checks directly on the processor and guard banks. 

### `Input`

 Site data and width bounds used by the shared-bit guard. 

### `Input.prog`

 Universal program whose literal prefix appears in the site input. 

### `Input.n`

 Length of the complete physical site input, including its padding. 

### `Input.u`

 Exponent giving the private instruction allowance as a power of the input length. 

### `Input.lit`

 Natural literal loaded as the private computation’s initial state word. 

### `Input.v`

 Site address encoded in the public address width. 

### `Input.hdr`

 Four-bit header accompanying the site address on the input. 

### `Input.sends`

 Shared send arrays that determine the site’s incident bits and successor checks. 

### `Input.initialWord`

 Initial-state literal packed into a word of the site’s RAM width. 

### `Input.prepared`

 The public half is exactly the output of `recordStartup_runs`. 

### `Input.valid`

 Both the sent and received successor fields satisfy their respective checks at the selected
site. 

### `Input.guarded`

 Actual continuation bank. Every update is local to the named guard ports. 

### `Input.readSteps`

 Step count of the successor-field scan, with predecessor presence determined by whether the
site address is positive. 

### `checked_count`

 Rejection contributes zero. A valid pair reaches the continuation once, after two guard pops. 

### `checked_allStops`

 Three guard ticks suffice for either rejection path. On a valid pair the extra tick
is passed to the continuation. 

### `guarded_registers`

 Cost, state, record, presence and remaining incident bits at the guard's normal return. 
