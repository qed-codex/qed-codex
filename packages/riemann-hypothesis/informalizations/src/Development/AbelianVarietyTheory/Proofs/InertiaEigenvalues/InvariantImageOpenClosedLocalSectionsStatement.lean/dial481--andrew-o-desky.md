---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/InvariantImageOpenClosedLocalSectionsStatement.lean",
  "declarations": [
    "GlobalTheory.T.invariant_image_openClosed_local_sections"
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

## Local sections and properness for nonsingular Hermitian invariants

[Theorem REP.0845](https://andrewodesky.com/rh/lean/GlobalTheory.T.invariant_image_openClosed_local_sections/)

Let $F,E$ be locally compact nontrivially normed ultrametric fields of characteristic zero, with a normed $F$-algebra structure on $E$ and $[E:F]=2$. Let $x\mapsto\bar x$ be a nontrivial involution of $E$ fixing $F$, preserving the norm, and satisfying $\{|x|:x\in E\}=\{|a|:a\in F\}$. Fix $r\ge0$. Put $$\mathcal H_r=\{(A,u,d):A=A^*\in M_r(E),\ u\in E^r,\ d\in F\},\qquad \mathcal I_r=F^r\times F^r\times F.$$ For $X=(A,u,d)$, its invariant $a=(c,b,d)$ is specified by $$\det(TI-A)=T^r+\sum_{i=0}^{r-1}c_iT^i,\qquad b_i=u^*A^iu\quad(0\le i<r).$$ Define $\Delta(a)$ in the conventions. Fix $a_0$ with $\Delta(a_0)\ne0$.

If $a_0$ is not the invariant of a point of $\mathcal H_r$, the same holds for every $a$ in some neighborhood of $a_0$. If it is such an invariant, there are a compact open neighborhood $\Omega\ni a_0$ and a map $s:\mathcal I_r\to\mathcal H_r$, continuous on $\Omega$, such that $s(a)$ has invariant $a$ and $\Delta(a)\ne0$ for every $a\in\Omega$. Moreover, for every compact $C\subseteq\mathcal H_r$, $$\{(g,a)\in U(r,E/F)\times\mathcal I_r:a\in\Omega,\ g\cdot s(a)\in C\}$$ is compact, where $g\cdot(A,u,d)=(gAg^*,gu,d)$ and $U(r,E/F)=\{g:g^*g=gg^*=I\}$.
