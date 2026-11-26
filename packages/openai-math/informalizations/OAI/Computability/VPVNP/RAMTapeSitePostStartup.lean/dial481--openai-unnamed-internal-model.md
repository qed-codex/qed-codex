---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSitePostStartup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSitePostStartup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSitePostStartup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Entering the sorting pass on a completed local record buffer

The site carries the public word and address widths, the unary slot count,
the completed block, the remaining incident suffix, and the two boundary
records. Two new unary counters initialize the sorting scheduler and its
row visits. All other data stay at their actual ports.


### `rowWidthPort`

 Unary row-width counter holding the ceiling binary logarithm of the slot count. 

### `remainingPort`

 Unary count initialized to the sorting row width plus the site address width for the
schedule. 

### `preparePorts`

 Connect sorting startup to the retained address width and slot count, its scratch ports,
and the two new scheduler counters. 

### `prepare`

 Initialize the local sorting scheduler and row-width counter on the physical post-pass
bank. 

### `prestate`

 Stack bank before initialization, immediately after the record block
has been closed and the two successor fields have been extracted. 

### `prestate_ports`

 The actual nonempty ports at the handoff. The initial block and two
boundary records may contain arbitrary raw words. 

### `rawBank`

 An untyped view of the call-to-sort handoff, for installing these ports
into the surrounding processor. The other stacks start empty. 

### `prepareSort`

 The sorter shares the predecessor and successor record ports with
the terminal scan through the surrounding bank. 

### `prepareSort_emitted`

 Use exactly the five-word encodings left by the record emitter. 

### `prepareSort_messages`

 Starting at the call-to-sort handoff, execute the scheduler and retain
the two physical boundary records for the final predecessor check. 
