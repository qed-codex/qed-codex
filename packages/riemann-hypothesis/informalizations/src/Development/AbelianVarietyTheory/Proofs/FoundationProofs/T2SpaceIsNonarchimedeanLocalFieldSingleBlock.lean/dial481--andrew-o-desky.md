---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/T2SpaceIsNonarchimedeanLocalFieldSingleBlock.lean",
  "declarations": [
    "GlobalTheory.SingleBlock.localIntegralSingleBlock"
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

## A local matrix coefficient and its integral from one congruence block

[Theorem REP.0744](https://andrewodesky.com/rh/lean/GlobalTheory.SingleBlock.localIntegralSingleBlock/)

Let $F$ be a nonarchimedean local field with its Borel measurable structure, ring of integers $O$, uniformizer $\varpi\in O$, residue field of order $q$, and normalized absolute value $|\varpi|=q^{-1}$. Let $r,t\ge0$. Let $\mu,\eta:F^\times\to\mathbb C^\times$ be characters, with $\mu$ trivial on $1+\varpi O$ and $\eta$ unramified and unitary. Let $$1+\varpi M_r(O)\subseteq P\subseteq\operatorname{GL}_r(O),$$ where the first group means the kernel of reduction in $\operatorname{GL}_r(O)$. Let $\lambda:P\to\mathbb C^\times$ be trivial on that kernel. On $M_{r+t,r}(F)$ define $$\Phi\binom XY=\begin{cases}\lambda(X)\mu(\det X)^{-1},&X\in P,\ Y\in\varpi M_{t,r}(O),\\0,&\text{otherwise}.\end{cases}$$ Normalize additive Haar measure $\nu$ so that $M_{r+t,r}(O)$ has volume $1$, and put $I(f,h)=\int f(z)\overline{h(z)}\,d\nu(z)$ and $c=I(\Phi,\Phi)$. Define $$\omega(g,h)f(z)=\mu(\det g)\eta(\det g)\mu(\det h)^{-1}|\det g|^{(r+t)/2}|\det h|^{-r/2}f(h^{-1}zg).$$ Then $\Phi$ is locally constant with compact support and $$c=|\overline P|q^{-r^2-rt},\qquad I(\omega(g,1)\Phi,\Phi)=\begin{cases}\lambda(g)c,&g\in P,\\0,&g\notin P,\end{cases}$$ where $\overline P$ is the image of $P$ in $\operatorname{GL}_r(O/\varpi O)$. For normalized additive Haar measures $\nu_1,\nu_2$ on $M_r(F),M_{t,r}(F)$, one also has $c=\nu_1(P)\nu_2(\varpi M_{t,r}(O))$.

Let $J$ be the set of $h\in\operatorname{GL}_{r+t}(O)$ whose top-left block is congruent modulo $\varpi$ to an element of $P$ and whose bottom-left block is zero modulo $\varpi$. This set is a subgroup. For every $h\in J$, its top-left block $h_{11}$ belongs to $P$ and $$\omega(1,h)\Phi=\bigl(\lambda(h_{11})\mu(\det h_{11})^{-1}\mu(\det h)\bigr)^{-1}\Phi.$$ Moreover $$[\operatorname{GL}_{r+t}(O):J]c=\prod_{i=t+1}^{r+t}(1-q^{-i})=\left(\prod_{i=t+1}^{r+t}(1-q^{-i})^{-1}\right)^{-1}.$$

Let $\sigma$ be a complex representation of $\operatorname{GL}_r(F)$ on an inner-product space, preserving its inner product. If $x_1,x_2$ are vectors with $\sigma(k)x_1=\lambda(k)x_1$ for $k\in P$, then for every Haar measure $dg$ the following integrand is integrable and $$\int_{\operatorname{GL}_r(F)}I(\omega(g,1)\Phi,\Phi)\overline{\langle x_2,\sigma(g)x_1\rangle}\,dg=\operatorname{vol}_{dg}(P)c\,\overline{\langle x_2,x_1\rangle}.$$ With $\operatorname{vol}_{dg}(P)=1$, the right side is $c\,\overline{\langle x_2,x_1\rangle}$.
