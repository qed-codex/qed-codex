---
{
  "module": "src/CompanionTheory/HarishChandraModules/LowKTypeMultiplicity/EigenspaceCyclicDensity/CreationOperators/KoszulDifferentialAnticommutator.lean",
  "declarations": [
    "CompanionTheory.D.LK.koszul_differential_sq_zero"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## A boundary operator from compact-root relations squares to zero

[Theorem ALG.1433](https://andrewodesky.com/rh/lean/CompanionTheory.D.LK.koszul_differential_sq_zero/)

Let $n\ge0$, let $\varepsilon:\{1,\ldots,n\}\to\{\pm1\}$, and let $V$ be a complex vector space. Let $E_{ab}\in\operatorname{End}_{\mathbb C}(V)$ satisfy $$[E_{ab},E_{cd}]=\delta_{bc}E_{ad}-\delta_{da}E_{cb}\qquad(\varepsilon_a=\varepsilon_b,\ \varepsilon_c=\varepsilon_d).$$ Put $P=\{(a,b):a<b\}$, ordered lexicographically, and $C=\{(a,b)\in P:\varepsilon_a=\varepsilon_b\}$. On the vector space of functions $x:\mathcal P(P)\to V$, define $$s_i(A)=(-1)^{\#\{j\in A:j<i\}},$$ $$(a_ix)(A)=\begin{cases}0&i\in A,\\s_i(A)x(A\cup\{i\})&i\notin A,\end{cases}\qquad (c_ix)(A)=\begin{cases}s_i(A)x(A\setminus\{i\})&i\in A,\\0&i\notin A.\end{cases}$$ Let $E_{ab}$ also denote its pointwise action on these functions. Define $$d=\sum_{(a,b)\in C}E_{ab}a_{(a,b)}+ \sum_{\substack{a<b<c\\(a,b),(b,c)\in C}}c_{(a,c)}a_{(b,c)}a_{(a,b)}.$$ Then $d^2=0$.
