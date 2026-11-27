---
{
  "module": "Solution/EndStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Codex (GPT-6.2 Astra)",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "license": "CC-BY-4.0"
}
---

# One import makes the five end statements available

AI drafted this autoinformalization from the original source. It is open for mathematical review.

The nine-line solution file consists of a licence header, an import of `ThreeSumApsp.Statements.EndStatement` and a note identifying the corresponding challenge. The five proof terms are in the imported module. Following that import gives a more useful starting point than searching this short file for the individual theorem names. [Solution/EndStatement.lean lines 1–9](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Solution/EndStatement.lean#L1-L9) · [ThreeSumApsp/Statements/EndStatement.lean lines 32–44](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/EndStatement.lean#L32-L44)

Four of the proof terms have much the same shape. The Exact Triangle statement starts from the rounded word-RAM version of Theorem 19. The 3SUM, min-plus product and all-pairs shortest-path statements each select their own component of `wordRam_theorem_22_second`. Each then applies `endStatement` and discharges numerical side conditions with `norm_num`. This explains which result supplies each bound when several exponents are named in the challenge. [ThreeSumApsp/Statements/EndStatement.lean lines 36–55](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/EndStatement.lean#L36-L55) · [Challenge/EndStatement.lean lines 40–49](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L40-L49)

For zero-weight clique, $k$ remains a variable. The proof introduces $k$ and its lower-bound hypothesis, uses the natural-number inequality $\lfloor k/3\rfloor\le k$ after casting it to the rationals, and records $0\le k$. These facts support the arithmetic after applying `endStatement` to the zero-weight corollary. [ThreeSumApsp/Statements/EndStatement.lean lines 57–66](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/EndStatement.lean#L57-L66)

I read the solution file and the cited end statements. I did not build the project or trace the word-RAM constructions behind the imported results.
