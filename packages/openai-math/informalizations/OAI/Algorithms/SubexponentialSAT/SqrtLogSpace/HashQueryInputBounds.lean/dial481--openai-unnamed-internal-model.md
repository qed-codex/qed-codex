---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashQueryInputBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashQueryInputBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashQueryInputBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Physical input bounds for all attained greedy histories and every trial,
including losing candidates. All bounds concern literal retained words and
raw slots. No execution-time or successful-query bound is used. 

### `initial_bytes`

 The original serializer retains all slots, including repeats and zeros. 

### `serialized_bounds`

 A common cap on actual scalar parameters gives one fixed cube for all
initial, attained, and trial history streams. The index rank is unrestricted. 

### `history_budget`

 The explicit allowance required by the actual outer-run theorem, not
merely a bound on the length of an individual attained history. 

### `run_caps`

 One actual retained allowance L=16*S³ discharges all numeric premises of
RunSpace, including the complete reference stream and full mass accumulator. 

### `boundary_words`

 All persistent boundary words are covered, including the incumbent,
odometer, remaining outer counter and the full attained history. 

### `staged_source_words`

 Time callbacks need only the physically read source words. Unrelated
incumbents need no artificial cap here; prefix space uses boundary_words. 

### `staged_words`

 Literal native staging of any candidate, including a loser, obeys the
same fixed cap. Every stack is bounded, not only the six source ports. 

### `commonCap`

 One finite sum collects concrete numeric parameters and a physical
master-word allowance. Its definition contains no search or query time. 

### `staged_sources_commonCap`

 Every actual trial source has one explicit fixed polynomial before any
round or candidate is selected; the history premise identifies the attained run. 

### `querySourcePorts`

 Exact source ports read by the marked frontend; 706 is its actual flag. 

### `marked_source_words`

 The actual marker adapter restores699, creates the forward unary index705
and true flag706, and preserves all six physically staged source words. 

### `marker_input_prefix`

 The paid marker setup has a fixed polynomial prefix cap once the actual
caller words are bounded. Its time depends only on the current unary index. 

### `record_input_frame`

 Parser construction changes only320/321. The full retained workspace
therefore identifies every physical query source even when322 is arbitrary. 

### `record_input_sources`

 Source-only transport into the actual collector callback. No hypothesis
restricts the retained accumulator or unread record stream. 

### `record_marked_sources`

 The actual markInput output inherits all staged source bounds from Ready;
its only new source is the actual finite reference and its true mark flag. 

### `record_input_words`

 Space additionally charges the actual unread tail, current reference and
accumulator. The three caps are exactly those supplied by the collector's
prefix invariant when the outer retained allowance is16*S³. 

### `input_polynomial`

 Fixed-degree input substitution. Constants and degree are fixed before
any particular input or candidate is chosen. 
