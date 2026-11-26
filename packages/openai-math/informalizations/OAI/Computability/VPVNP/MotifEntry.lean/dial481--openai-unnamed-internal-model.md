---
{
  "module": "OAI/Computability/VPVNP/MotifEntry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifEntry.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifEntry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the entries of a grouped motif map

For the construction on page 21, the input at a party is a collection of
incident bit strings. Read their common selector sequence, check its full
width vector, then use each copy's demand and supply fields to look up one
parameter. The output list records multiplicities in the resulting monomial.


### `inputBits`

 Binary digits are numbered from the least significant end. 

### `paddedBit`

 Probe one position, returning a zero bit outside the supplied string. 

### `readField`

 Read consecutive bits by incrementing the probe position and combining
each bit with the remaining high part by one shift and one addition. 

### `readField_eq_sum`

 The input oracle is used only at the indicated little-endian positions. 

### `readField_inputBits`

 Decoding from the bit oracle gives the same digit as division and
remainder, even if the requested field is wholly or partly in the padding. 

### `readField_lt`

 The decoded value of an arbitrary field fits in the field width. 

### `fieldIndex`

 A typed field, suitable for indexing the table of a fixed base motif. 

### `fieldIndex_eq_padFields`

 Reading the indicated demand chunk agrees with the padding injection. 

### `meteredField`

 Record each probe and the fixed operations in the recursion.
Each nonempty field iteration pays for the width test, one padded probe,
the position increment, low-bit conversion, doubling, and addition. 

### `readTag`

 Locate one selector above the payload. 

### `payloadBits`

 The low bits of a supply coordinate are its payload. 

### `offset`

 Scan the widths preceding a copy to find the start of its payload field. 

### `decode`

 The code table can be searched even when some bit patterns are unused. 

### `anchor`

 Read the reference half-wire without using choice. 

### `consistent`

 Check a party's source and target ports, testing one copy at a time. 

### `selectors`

 Decode the anchor sequence, checking each tag against the fixed selector
table. Once decoded, the array can be indexed when computing payload offsets. 

### `extract`

 Read the local supply fields in copy order and check the total vector on
all edges. The last test also checks coordinates away from the current party. 

### `indices`

 Execute all the entry checks on bit-string inputs. The argument `c`
supplies the demand coordinate of each copy. 

### `indices_eq_groupedIndices`

 Correctness of the executable local parser against the grouped wire map. 

### `labels`

 Replace the indices by their fixed parameter-table names. Repeated names
are retained once per occurrence. 

### `DemandBits`

 Local demand inputs with one bit string on each incident half-wire. 

### `demandFields`

 Read a copy's fixed-size fields on the demand side, supplying zero bits
above the width of the desired demand. 

### `demandBits`

 Canonical bit strings for the two demand endpoints. 

### `describe`

 The entry algorithm for an entire local map, including demand padding.
A failed check returns `none`; success returns the ordered parameter names. 

### `describe_correct`

 Specializing the output monomial gives exactly the paper's grouped
local entry in every coefficient semiring. 

### `labels_monomial`

 Every successful description denotes a single integral monomial of
total degree at most the number of copies. 

### `scanCopies`

 Walk through the copies in order. A cons iteration charges the index step
and the result-list cons in addition to the computed entry's own work. 

### `widthPrefix`

 Scan prior selector entries to find one payload offset. A width read and
addition are charged at each iteration along with the index increment. 

### `tableLookup`

 Count the code-table comparisons until the first match. 

### `meteredIndex`

 A metered, typed field read. The counter uses indexed bit probes and
word operations on positions, loop counters, and fixed-width base fields. 

### `arrayRun`

 Build a random-access array once. Count the indexed writes and the
iterations of the construction loop, besides each cell's own operations. 

### `portRun`

 Scan both ends of the fixed edge list. Each incident port supplies its
input to the given field operation. Charge the loop, the endpoint tests, and
writing the results to the party's local table. 

### `selectorRun`

 Stage one stores the selector words on all local ports, checks their
agreement, and decodes the anchor's words into a random-access array. 

### `totalRun`

 Compute and compare every edge's total width, including edges not
incident to the party. 

### `nameRun`

 Once the selector array is known, collect both sets of incident fields
for one base copy and return the corresponding parameter-table entry. 

### `run`

 Run the three stages on any input, including malformed selectors.
The operation count includes the parameter lookup and each output-list cons. 

### `run_le`

 The bit-probe and word-operation bound has an absolute quadratic
exponent. Only the fixed motif tables enter the multiplicative constant. 

### `tapeProbe`

 Read one position by starting at the left end of a stored bit list.
Out-of-range positions return zero. Every advance pays for inspecting the
cell, decrementing the address, and moving to the next cell. 

### `Tape`

 Sequential storage for one input string of the specified width. 

### `Tape.readBits`

 Read the bit at finite index `i` in a motif tape whose length is known. 

### `Tape.ofBits`

 Construct a motif tape by listing the bits of a function on `Fin n` in index order. 

### `tapeRun`

 A sequential-tape implementation with a conservative allowance for every
indexed probe. The input length is the sum of the fixed motif's edge-string
lengths. Ordinary control and word operations are charged the same allowance. 

### `tapeAllowance`

 Each demand or supply probe in `tapeRun` fits in its reserved allowance. 

### `tapeRun_le`

 The rescan implementation has an absolute polynomial exponent even when
the input tapes contain malformed data. 
