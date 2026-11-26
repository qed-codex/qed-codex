---
{
  "module": "src/Formalism/LocalToGlobal/HermitianForms/ExtraSym.lean",
  "declarations": [
    "Formalism.L2.Forms.ColsFullS"
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

## Determinants, volumes and local column compatibility

[Definition / hypothesis ARAK.D162](https://andrewodesky.com/rh/lean/Formalism.L2.Herm.SymmetricHermitianColumns/)

Use ([Hermitian column levels and local modifications](https://andrewodesky.com/rh/lean/Formalism.L2.Herm.HermColsCh/)) and ([Symmetric finite levels and column identifications](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.FormsTiedSym/)), with the same entire underlying Hermitian datum, not a new choice of levels or representatives. Write $D_t$, $U_O$, $e_1$ and $\det\operatorname{cl}_{u,i}$ for the determinant group, subgroup, rational norm-one map and class maps of ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)). For finite adeles the integral $E$-algebra is the image of $\mathcal O_E\otimes_{\mathcal O_F}\widehat{\mathcal O_F}$ in $E\otimes_F\mathbb A_{F,f}$.

Hypothesis (determinants). Choose a surjective homomorphism $$d:U(1)(\mathbb A_f)\longrightarrow D_t$$ with open kernel, every element of which is integral at all finite places. The subgroup $U_O$ is exactly the image of integral norm-one finite adeles. For $z\in E$ with $z\bar z=1$ and $x\in U(1)(\mathbb A_f)$ whose determinant is the diagonal finite adelic image of $z$, require $d(x)=e_1(z)$. Initially and at every positive stage, if $\det x=\det y_c$, require $$\det\operatorname{cl}_{u,i}(c)=d(x).$$ For every $N$, self-dual lattices $L,L'\subset E^N$ for the standard Hermitian form, unitary finite adelic $g$ with $\widehat L'=g\widehat L$, and $x\in U(1)(\mathbb A_f)$ with $\det x=\det g$, require $$\operatorname{relDet}(N,L,L')=[d(x)]\quad\text{in }D_t/U_O.$$

Hypothesis (volume normalization). Use the signature, reference lattice and prescribed volume $\operatorname{vol}(W)$ of ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)) and ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), and the measures $c_{P,Q}$ of ([Moment data for the family](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.Draft.SData/)). For every Hermitian space $W$ whose recorded signatures are its actual complex signatures and equal $(P,Q)$, consider Haar measures $\mu$ on its full adelic unitary group compatible with the constant signature arrays $P_\tau=P$ and $Q_\tau=Q$, using the compatible-Haar-measure definition in the conventions of ([Original moduli uniformizations and cusp norms](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM/)). For every $\mu$ satisfying this normalization and every fundamental domain $\mathcal F$ for the rational unitary subgroup, require $$\mu(\mathcal F)=\operatorname{ofReal}(\operatorname{vol}(W)).$$ For every $1\le j\le m$, also require the recorded sign $\epsilon_j$ of ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)) to be $+1$.

Hypothesis (local polynomial group comparison). For every source, coefficient place and admissible local index, impose ([Local group completions and stabilizers](https://andrewodesky.com/rh/lean/Formalism.L2.Herm.GLevTie/)) on the same initial level and local parameter system. Here admissibility means the recorded predicate on $T_u$, the residual characteristic and the distinguished rational primes in ([Local parameter systems for the family](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NAut/)).

Use the integral comparison maps of ([Integral comparisons for theta chains](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.LatCmp/)), the local fields, automorphisms $\sigma_v$, embeddings $\iota_v$, maps $\operatorname{iw}_{0,v}$ and coefficient embedding $\operatorname{embW}$ of ([Local parameter systems for the family](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NAut/)) and ([Integral comparisons for theta chains](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.LatCmp/)). Use the additional data and integral and theta compatibility conditions for this arithmetic member in ([Integral and theta compatibility for families](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Extra/)). The initial level in these data equals this chosen initial level. Its two $\pi_g$, all $\pi_u$ and labelled $F$-places equal those of ([Hermitian column levels and local modifications](https://andrewodesky.com/rh/lean/Formalism.L2.Herm.HermColsCh/)), with the same subfield, norm and congruence conditions.

For every admissible source $u$, coefficient place $w$, local index $v$, secondary index $s$ and $a\in\mathcal O_F$, require $$a\in\mathfrak p_v\iff \operatorname{val}_w(\tau_{v,s}(a))>0,$$ where $\mathfrak p_v$ is the place chosen in ([Local group completions and stabilizers](https://andrewodesky.com/rh/lean/Formalism.L2.Herm.GLevTie/)) and $\tau_{v,s}:E\to K$ is the prescribed CM embedding. For every $x\in E$, the chosen isomorphism from the local coefficient ring to the completion at $\mathfrak p_v$ sends $\operatorname{iw}_{0,v}(x)$ to the first component of the chosen splitting of $x$ in $E\otimes_FF_{\mathfrak p_v}$. Require also $$\iota_v\bigl(\sigma_v^s(\operatorname{iw}_{0,v}(x))\bigr)=\operatorname{embW}\left(\tau_{v,s}\left(\begin{cases}\bar x,&s\text{ odd},\\x,&s\text{ even}\end{cases}\right)\right).$$ All indices, embeddings and fields in these identities are the existing chosen ones, and the conditions hold at every admissible source and coefficient place.
