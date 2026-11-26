---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/CuspFormsExtendVanishCompactifiedFlagSpaceStatement.lean",
  "declarations": [
    "GlobalTheory.T.cuspForms_extend_vanish_compactifiedFlagSpace"
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

## Extension of cusp forms with boundary vanishing

[Theorem AGR.1462](https://andrewodesky.com/rh/lean/GlobalTheory.T.cuspForms_extend_vanish_compactifiedFlagSpace/)

Fix the member data in ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)). Use ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)) for its CM field $E$, quadratic subfield $E_0$, generator primes, primitive ideal and invariant different factor. Assume ([Polarized modules and unitary moduli](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)), ([Coefficient fields and deeper moduli levels](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Level/)), ([Complex uniformizations and period lattices](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FD.Data/)), ([Adelic frames for unitary moduli](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.Core/)), and ([Flag models and logarithmic Kodaira–Spencer maps](https://andrewodesky.com/rh/lean/GlobalTheory.CompHS.TorFlag/)) for the same chosen stage $j\ge0$. Let $(p_{\rm sig},q_{\rm sig})$ be that stage's signature and $r=p_{\rm sig}+q_{\rm sig}$ its rank. The moduli square root $\rho$ and prime $d_{\rm mod}$ need not equal the arithmetic $s_d,d$. Assume $\lfloor[E:\mathbb Q]/2\rfloor>2$.

Let $B/K$ and $\pi:\mathcal F\to B$ be any compactified model and flag model satisfying ([Flag models and logarithmic Kodaira–Spencer maps](https://andrewodesky.com/rh/lean/GlobalTheory.CompHS.TorFlag/)), with $\jmath:X\hookrightarrow B$ its dense moduli open. For every irreducible component $Z$ of $X$, put $$B_Z=B\setminus\overline{\jmath(X\setminus Z)},\qquad \mathcal F_Z=\pi^{-1}(B_Z),\qquad \mathcal U_Z=\mathcal F_Z\cap\pi^{-1}(\jmath(X)).$$ For $\tau\in\Psi$, let $F_\tau^i$ ($0\le i\le p_{\rm sig}$) and $F_{\bar\tau}^i$ ($0\le i\le q_{\rm sig}$) be the tangent flags, each spanned locally by the first $i$ tangent-frame vectors, and put $Q_{\tau,i}=F_\tau^{i+1}/F_\tau^i$ and $Q_{\bar\tau,i}=F_{\bar\tau}^{i+1}/F_{\bar\tau}^i$. Here $\bar\tau$ is the complex-conjugate embedding. A weight is any integer array $\lambda=(\lambda_{\tau,i})_{\tau\in\Psi,\,0\le i<r}$. Its line bundle is $$\mathcal L_\lambda=\bigotimes_{\tau\in\Psi}\left( \bigotimes_{i=0}^{p_{\rm sig}-1}Q_{\tau,i}^{-\lambda_{\tau,i}} \otimes\bigotimes_{i=0}^{q_{\rm sig}-1}Q_{\bar\tau,i}^{\lambda_{\tau,r-1-i}}\right).$$ Write $\mathcal L_{\lambda,Z}$ for its restriction to $\mathcal F_Z$.

Every cusp form $f$ of weight $\lambda$ supported on $Z$ has an associated section $s_f$ on $\mathcal U_Z$ and an extension $$\widetilde s_f\in H^0(\mathcal F_Z,\mathcal L_{\lambda,Z}),\qquad \widetilde s_f|_{\mathcal U_Z}=s_f,$$ whose germ lies in the maximal ideal at every point of $\mathcal F_Z\setminus\mathcal U_Z$, in every line-bundle trivialization. Supported on $Z$ means that the form evaluates to zero on every framed point over every coefficient algebra whose whole image lies off $Z$. Here cusp forms are the algebraic automorphic sections whose pullbacks at every permitted coefficient embedding belong to the complex span of holomorphic cusp forms of the induced domain weight; the domain weight, arbitrary-algebra evaluation and the cusp condition are those of ([Complex uniformizations and period lattices](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FD.Data/)).
