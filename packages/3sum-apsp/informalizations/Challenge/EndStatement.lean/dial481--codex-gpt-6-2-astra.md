---
{
  "module": "Challenge/EndStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Codex (GPT-6.2 Astra)",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "license": "CC-BY-4.0"
}
---

# Five running times on a deterministic word RAM

AI drafted this autoinformalization from the original source. It is open for mathematical review.

A time bound here comes with an input convention. Choose the exponent $κ$ bounding the absolute values of input integers by $n^κ$. The statement then supplies a program, a word-length constant and a time bound. The program must return the right answer for every admissible input and every sufficiently large word size, starting at a constant times $\lfloor\log_2 n\rfloor+1$ bits. Correctness includes small inputs; the asymptotic time estimate starts at $n=2$. [EndStatement.lean lines 11–20](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L11-L20) · [EndStatement.lean lines 22–35](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L22-L35)

The five challenge targets use this convention in different ways.

- **Exact Triangle and 3SUM.** The triangle problem on three square integer matrices has exponent $3-0.0017$. For 3SUM the question is whether entries at three different positions sum to zero. Its time exponent is $1.9992$. [EndStatement.lean lines 56–64](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L56-L64)
- **Min-plus product and all-pairs shortest paths.** Both receive exponent $2.99942$. The path problem allows missing directed edges and assumes there is no negative cycle; if a pair has no path its distance cell is unconstrained. [EndStatement.lean lines 36–46](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L36-L46) · [EndStatement.lean lines 66–74](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L66-L74)
- **Zero-weight clique.** For $k\ge3$ parts with $n$ vertices per part, the decision bound has exponent $k-0.0017\lfloor k/3\rfloor$. For example, at $k=6$ the exponent is $6-0.0034$, because there are two whole groups of three parts. [EndStatement.lean lines 76–80](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L76-L80)

I read this challenge file. Its five theorem bodies are placeholders for comparison with a solution. I did not build the project or audit the underlying algorithms. [EndStatement.lean lines 54–81](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L54-L81)
