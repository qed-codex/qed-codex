---
{
  "module": "src/Formalism/LocalToGlobal/ProjectiveLattices/VAddIntNonneg.lean",
  "declarations": [
    "Formalism.L2.Pj.IsVal",
    "Formalism.L2.Pj.latOf"
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

## Finite-place valuation families and integral submodules

[Definition / hypothesis ARAK.D032](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.IsVal/)

These definitions turn families of finite-place evaluations into integral submodules.

**Valuation families.** Let $K$ be a number field, let $\mathcal F$ be a commutative $K$-algebra, and write $v_\lambda$ for the integer valuation at a finite prime $\lambda$ of $K$. A function $v:\mathcal F\to\mathbb R\cup\{+\infty\}$ has the required valuation properties at $\lambda$ if, for every $f,g\in\mathcal F$ and $a\in K^\times$, $$v(0)=+\infty,\qquad v(f+g)\ge\min(v(f),v(g)),\qquad v(fg)=v(f)+v(g),$$ $$v(af)=v_\lambda(a)+v(f).$$ The function constantly equal to $+\infty$ is allowed. A family $\mathcal V$ chooses, for each $\lambda$, a possibly empty set $\mathcal V_\lambda$ of such functions. For a $K$-vector subspace $W\subseteq\mathcal F$, its associated integral $\mathcal O_K$-submodule is $$\Lambda(W;\mathcal V)=\{f\in W:v(f)\ge0\text{ for every }\lambda\text{ and every }v\in\mathcal V_\lambda\}.$$

**Ordinary integral evaluations.** Take a moduli scheme $X$ and coefficient number field $K\subset\mathbb C$ with the moduli and coefficient-field choices of ([Polarized modules and unitary moduli](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)) and ([Coefficient fields and deeper moduli levels](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Level/)). Use the integral-framed-point definition and fixed-presentation evaluation of ([Integral evaluation of moduli sections](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM.evalWD/)), with $(X,K)$ in place of the original $(X_j,K_0)$. Here $\mathcal F$ is the $K$-algebra of scalar rules, with pointwise operations.

For each $\lambda$, range over all characteristic-zero complete DVRs $R$ with finite residue field, fraction fields $L$, embeddings $\iota:K\hookrightarrow L$, positive integers $e$ such that $$v_R(\iota(a))=e\,v_\lambda(a)\qquad(a\in K^\times),$$ and integral framed points $y$ over $(R,L,\iota)$. The ordinary family $\mathcal R_\lambda$ consists of all functions $$f\longmapsto v_{R,e}(f(y)),$$ where $v_{R,e}$ is the normalized extended evaluation valuation in ([Integral evaluation of moduli sections](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM.evalWD/)). In particular, a zero evaluation has value $+\infty$.

**Primewise selection.** Given two families $\mathcal V',\mathcal V''$ and a set $S\subseteq\mathbb N$, define $$\mathcal V^S_\lambda=\begin{cases} \mathcal V'_\lambda,&\text{some }n\in S\text{ has image in }\lambda,\\ \mathcal V''_\lambda,&\text{otherwise}. \end{cases}$$ For a set of rational primes $S$, the first case means that the residue characteristic of $\lambda$ belongs to $S$.

For a number field $E$, a positive integer $M'$ and a real $B$, the selected-prime set is $$S_B(E,M')=\{\ell:\ell\text{ is prime and }(\ell\le B\text{ or }\ell\mid2|\operatorname{disc}E|M')\}.$$ For a level $(M,\mathfrak b,A)$ of ([Coefficient fields and deeper moduli levels](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Level/)), use $M'=\operatorname{lcm}(M,A)$.
