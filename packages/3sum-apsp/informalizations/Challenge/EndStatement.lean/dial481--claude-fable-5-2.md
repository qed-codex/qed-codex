---
{
  "module": "Challenge/EndStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude Fable 5.2",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "license": "CC-BY-4.0"
}
---

# Informalization of Challenge/EndStatement.lean: five running-time claims for 3SUM, shortest paths and related problems

**This file states five theorems and proves none. They are claims of a paper by Josh Alman and Virginia Vassilevska Williams, stated for deterministic programs of a word RAM with words of $O(\log n)$ bits, on integers of absolute value at most $n^{\kappa}$ for every fixed $\kappa$: Exact Triangle in time $O(n^{3 - 0.0017})$, 3SUM in time $O(n^{1.9992})$, the (min,+)-product and all-pairs shortest paths in time $O(n^{2.99942})$, and Zero-Weight $k$-Clique in time $O(n^{k - 0.0017 \lfloor k/3 \rfloor})$ for every $k \ge 3$.** All five end in `sorry`. The machine, the problems and the meaning of "solved in time" are defined in a second file, the `EndStatement.lean` at the root of the project, which I read as well. Below, `EndStatement.lean` without a folder means that root file.

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## What kind of file this is

The file has 82 lines. It imports the root file `EndStatement.lean` and nothing else. [Line 6](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L6) Its header says what that file does: it defines a word RAM, says what it means that a problem is solved within a time bound, and states five claims of the paper as propositions. [Lines 8–13](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L8-L13) `EndStatement.lean` names the paper, "Truly Subquadratic 3SUM and Truly Subcubic APSP via Triangles in Sparse Lopsided Graphs", and its two authors. It says of itself that it imports nothing and proves nothing. [EndStatement.lean, lines 8–9](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/EndStatement.lean#L8-L9)

The five theorems are in the namespace `ThreeSumApsp`. Each has the body `sorry`. [Lines 54–82](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L54-L82) A Comparator configuration of the project names this file as the challenge and `Solution.EndStatement` as the module that has to prove the same five statements. It permits the axioms `propext`, `Quot.sound` and `Classical.choice`. [comparator-endstatement.json, lines 1–18](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/comparator-endstatement.json#L1-L18) I have not built the project and have not run Comparator.

The project has a second, long statement file, `PaperStatements.lean`, for further results of the paper. This note does not cover it. [README, line 7](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/README.md?plain=1#L7)

## The machine

Memory cells are named by integers, negative ones included. Each cell holds a word of $W$ bits. A program is a list of instructions of nine kinds: write the constant $1$ into a cell; add, subtract or multiply two cells and write the result into a cell; load from the cell whose name is the content of a cell; store to such a cell; jump to a fixed position of the program if a word is negative; accept; reject. [EndStatement.lean, lines 15–25](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/EndStatement.lean#L15-L25)

Each instruction takes one step, and the halting step is counted. A word that is used as the name of a cell is read as a signed number. Arithmetic is that of $W$-bit words. A program that runs past its end rejects. [EndStatement.lean, lines 27–42](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/EndStatement.lean#L27-L42) At the start a list of integers stands in cells $0, 1, 2, \dots$ and every other cell holds $0$. The integers are stored as words of $W$ bits, that is, modulo $2^W$. [EndStatement.lean, lines 44–46](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/EndStatement.lean#L44-L46)

## What "solved in time $O(n^r)$" means

- **The bound.** For $r \ge 0$, as in the five claims, `BigO T r` says that there is a constant $K$ with $T(n)^{q} \le K n^{p}$ for all $n \ge 2$, where $r = p/q$ in lowest terms. The definition accepts every rational $r$; for a negative $r$ it puts $0$ in place of $p$. This is $T(n) = O(n^r)$ written without fractional powers. [EndStatement.lean, lines 48–51](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/EndStatement.lean#L48-L51)
- **A problem.** A problem has, for each size $n$, a set of instances. Each instance is written as a list of integers. A problem may fix when to accept. If it does not, the program has to accept. A problem may also fix a condition on the cells after the input. [EndStatement.lean, lines 53–58](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/EndStatement.lean#L53-L58)
- **One run.** The memory starts with $n$ in cell $0$ and the input after it. The program has to halt within $t$ steps. It has to accept exactly when the instance is a yes-instance, and the cells after the input, read as signed numbers, have to satisfy the output condition. [EndStatement.lean, lines 60–63](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/EndStatement.lean#L60-L63)
- **Solved in time.** For every natural number $\kappa$ there are one program, one number $b$ and one function $T$ with $T(n) = O(n^r)$ such that the following holds. On every instance of every size $n$ whose numbers have absolute value at most $n^{\kappa}$, and at every word size $W \ge b (\lfloor \log_2 n \rfloor + 1)$, the run succeeds within $T(n)$ steps. [EndStatement.lean, lines 65–70](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/EndStatement.lean#L65-L70)

The program, $b$ and $T$ may depend on $\kappa$. They do not depend on $n$, on the instance or on the word size.

## The five problems and the five claims

1. **Exact Triangle.** The input is three $n \times n$ matrices of integers, written row by row. The answer is yes if there are $a, b, c$ with $w_{AB}(a,b) + w_{BC}(b,c) + w_{AC}(a,c) = 0$. The claim is time $O(n^{3 - \varepsilon_T})$ with $\varepsilon_T = 0.0017$. [EndStatement.lean, lines 72–86](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/EndStatement.lean#L72-L86) [Lines 56–59](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L56-L59)
2. **3SUM.** The input is $n$ integers. The answer is yes if three of them, at three different positions, sum to $0$. The claim is time $O(n^{1.9992})$. [EndStatement.lean, lines 88–96](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/EndStatement.lean#L88-L96) [Lines 61–64](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L61-L64)
3. **The (min,+)-product.** The input is two $n \times n$ matrices $A$ and $B$ of integers. The program has to accept, and the output, row by row, is the matrix whose entry $(i, j)$ is the least of the sums $A_{ik} + B_{kj}$. The claim is time $O(n^{2.99942})$. [EndStatement.lean, lines 98–107](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/EndStatement.lean#L98-L107) [Lines 66–69](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L66-L69)
4. **All-pairs shortest paths.** The instance is a directed graph on $n$ vertices with integer weights on its edges, in which every closed path has weight at least $0$. The input is the 0/1 matrix of the edges and then the matrix of the weights, with $0$ where there is no edge. The program has to accept, and the output has two cells for each pair $(i, j)$: either $1$ and the least weight of a path from $i$ to $j$, or $0$ if there is no path. A path may repeat vertices, and it may be empty, so the distance from $i$ to $i$ is $0$. The claim is time $O(n^{2.99942})$. [EndStatement.lean, lines 109–126](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/EndStatement.lean#L109-L126) [Lines 71–74](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L71-L74)
5. **Zero-Weight $k$-Clique.** There are $k$ parts of $n$ vertices each. The input is an $n \times n$ block of weights for each of the $k^2$ ordered pairs $(i, j)$ of parts, row by row. Only the blocks with $i < j$ count. The answer is yes if one vertex can be chosen in each part so that the weights of the $\binom{k}{2}$ pairs sum to $0$. The claim is, for every $k \ge 3$, time $O(n^{k - \varepsilon_T \lfloor k/3 \rfloor})$. [EndStatement.lean, lines 128–137](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/EndStatement.lean#L128-L137) [Lines 76–80](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L76-L80)

## The reading notes in the header

The header of this file lists points on how `EndStatement.lean` is to be read. [Lines 22–51](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L22-L51) Among them:

- The machine is generous on three points, and the header says that none of them changes an exponent. Every cell other than cell $0$ and the cells of the input holds $0$ at the start, and no space is charged. The cells that a program names in its text are arbitrary integers and need not be addressable by a word. The constant $b$ is chosen after $\kappa$. [Lines 23–26](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L23-L26)
- The answer has to be right at every size $n$, with $n = 0$ included, where $\lfloor \log_2 0 \rfloor$ is read as $0$. The time bound binds from $n = 2$ on. [Lines 27–30](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L27-L30)
- $\kappa = 0$ is included, where the paper's Theorem 19 and Corollary 39 have an exponent of at least $1$. The bound $n^{\kappa}$ is asked of every number of the input. That includes the entries $0$ and $1$ of the edge matrix in the shortest-path problem and the blocks of the clique problem that do not count. Where there is no path, the cell for the distance is free. [Lines 31–39](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L31-L39)
- How an instance is written into the cells is fixed in `EndStatement.lean` and not in the paper. [Lines 36–38](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L36-L38)
- The paper's Theorem 22 prints two rounded exponents for each of its three problems, by two routes. The claims here take the smaller ones: $1.9992$ for 3SUM, where the other is $1.99923$, and $2.99942$ for the other two, where the other is $2.99949$. [Lines 42–47](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L42-L47)

## What the statements leave out

- **Proofs.** This file has none.
- **The constants.** The claims say that a program, a constant $b$ and a bound exist. The README says that the constants of the time bounds are not optimized, that they are large, and that for most theorems no value is given. [README, line 61](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/README.md?plain=1#L61)
- **Other results of the paper.** The README has a table of what is proved in which form. Its last row, on what is not proved for any machine, includes the running times for real inputs. [README, lines 9–16](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/README.md?plain=1#L9-L16)
- **The version of the paper.** The README says that the text follows version 1 of the paper on arXiv, arXiv:2610.06783v1. [README, line 24](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/README.md?plain=1#L24)

## What I read

I read this file and `EndStatement.lean` in full, the Comparator configuration, and lines 1 to 65 of the README, at the linked revision. I did not read the paper. I did not read the proofs, and I did not build the project.
