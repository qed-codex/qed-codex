---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/VolumeRatioOfUnfolding.lean",
  "declarations": [
    "GlobalTheory.VolRatioUnfold.volumeRatio_of_unfolding"
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

## The adelic volume ratio on removing a unit vector

[Theorem ANT.1486](https://andrewodesky.com/rh/lean/GlobalTheory.VolRatioUnfold.volumeRatio_of_unfolding/)

Choose an arithmetic datum satisfying ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), with CM extension $E/F$, $f=[F:\mathbb Q]$ and positive volume assignment $V\mapsto\operatorname{vol}(V)$. Hermitian spaces with recorded lattice data have the generic meaning in ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)). Assume the following volume normalization: for every such space $V$ whose recorded signatures are correct and constant, say $(P,Q)$, there is a compatible Haar measure $\eta$ on $U(V)(\mathbb A_F)$; for every such $\eta$ there is a rational fundamental domain, and every such domain $\mathcal F$ satisfies $$\eta(\mathcal F)=\operatorname{vol}(V).$$ Compatibility and rational fundamental domains are specified in the conventions below. Put $v=|\operatorname{disc}E|^{1/[E:\mathbb Q]}/2$.

Let $W$ be a Hermitian space with these recorded data, of rank $m\ge3$, whose Gram matrix has its recorded signature $(P,Q)$ at every complex embedding of $E$. Let $s\in\{1,-1\}$, with $P\ge1$ if $s=1$ and $Q\ge1$ if $s=-1$. There are $x\in W$ with $h(x,x)=s$ and a Hermitian space $W'$ with recorded lattice data, embedded $E$-linearly and isometrically onto $x^\perp$, whose Gram matrix has its recorded signature $(P-1,Q)$ if $s=1$ and $(P,Q-1)$ if $s=-1$ at every complex embedding of $E$, such that $$\frac{\operatorname{vol}(W')}{\operatorname{vol}(W)} =\left(\frac{(2\pi)^m}{(m-1)!}\right)^f \frac{((2v)^f)^{1/2-m}}{\mathcal L_E(m)}.$$ Here $\mathcal L_E(m)=\prod_{\mathfrak p}e_{\mathfrak p}(m)$, over maximal ideals of $\mathcal O_E$, with $N\mathfrak p=|\mathcal O_E/\mathfrak p|$ and $$e_{\mathfrak p}(m)= \begin{cases} (1-(-1)^m(N\mathfrak p)^{-m/2})^{-1},&\overline{\mathfrak p}=\mathfrak p,\\ (1-(N\mathfrak p)^{-m})^{-1/2},&\overline{\mathfrak p}\ne\mathfrak p. \end{cases}$$
