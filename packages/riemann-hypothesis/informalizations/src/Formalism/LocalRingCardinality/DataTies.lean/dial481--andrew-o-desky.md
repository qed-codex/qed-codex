---
{
  "module": "src/Formalism/LocalRingCardinality/DataTies.lean",
  "declarations": [
    "Formalism.BasicNotions.Ties"
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

## Period, measure and twist comparisons

[Definition / hypothesis PHT.D151](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Ties/)

Hypothesis (period and measure comparisons). Use the fields and rank data of ([Local congruence tables](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)), the spaces and type labels of ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)), the period pairings of ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)), and the moment datum of ([Moment data for the family](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.Draft.SData/)). The six following conditions are imposed at every family member.

For every sign vector $\epsilon$ with $p$ positive and $q$ negative signs, and every bijection $e$ from positive-then-negative coordinate labels to the coordinates with sign vector $\epsilon$ that preserves each sign, the scaled measure $s_{p+q,\epsilon}\mu^0_\epsilon$ in the moment datum agrees with the column datum's Haar measure $\mu^{\rm cd}_{p,q}$ after matrix reindexing. Explicitly, for every measurable subset $B$ of the sign-vector unitary group, $$s_{p+q,\epsilon}\mu^0_\epsilon(B)=\mu^{\rm cd}_{p,q}\{g:\operatorname{reindex}_e(g)\in B\}.$$ Here matrix reindexing replaces row and column labels by $e$; the measures and their normalizations are those of ([Formal degree with compact-dual normalization](https://andrewodesky.com/rh/lean/PositivityTheory.RgFd.B.formalDegreeCompactDual/)).

For each $\tau\in\Sigma$, form the rank-$r$ parameter and sign vector $$\lambda_\tau=(V_{\tau,0},\ldots,V_{\tau,k-2},-B_{\tau,0},\ldots,-B_{\tau,m-1}),$$ with positive signs in the first $k-1$ positions and then alternating positive and negative signs. Let $\rho_c$ and $\rho_n$ be half the sums of the roots $e_i-e_j$, $i<j$, whose two coordinates have respectively equal and different signs. Put $\Lambda_\tau=\lambda_\tau+\rho_n-\rho_c$. Whenever an irreducible continuous unitary square-integrable representation on a nonzero complex Hilbert space has a compact type of highest weight $\Lambda_\tau$, and every compact-type highest weight $\mu$ satisfies $\|\Lambda_\tau+2\rho_c\|^2\le\|\mu+2\rho_c\|^2$, every positive formal degree for $s_{r,\epsilon}\mu^0_\epsilon$ equals the designated number $d_\tau$. The compact group is the subgroup preserving the positive and negative coordinate subspaces. Formal degree $d$ means that all products below are integrable and $$\int\langle w,\pi(g)v\rangle\overline{\langle w',\pi(g)v'\rangle}\,d(s_{r,\epsilon}\mu^0_\epsilon)(g)=\frac{\langle v',v\rangle\langle w,w'\rangle}{d}$$ for all vectors, with the Hermitian convention linear in the second variable.

For a type $\mu$, let $V^0_\mu$ be the degree-zero subspace of its ambient space $A_\mu$, and $U_\mu=V^0_\mu\cap\ker i_\mu$, where $i_\mu:A_\mu\to H$ is the linear map of ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)). The restriction of $i_\mu$ to $Q_\mu=V^0_\mu\cap U_\mu^\perp$ is injective. Define $s_\mu:H\to A_\mu$ by orthogonal projection onto $i_\mu(Q_\mu)$ followed by the inverse of that restriction. For every source $u$, every source vector $\phi$ and every $x\in H$, require $$B_u(\phi,x)=P_{u,\mu_0}(\phi,s_{\mu_0}(x)).$$

The base coefficient field $K_0\subset K$ is Galois over $\mathbb Q$. Every place $v$ of $K_0$ above a rational prime $p$ that is induced by a twisted place of $K$ is induced by one of the two prescribed embeddings of a twist coefficient ring: there is a twist index $i$ with residue characteristic $p$ such that, for all $x\in\mathcal O_{K_0}$, either $$x\in\mathfrak p_v\quad\Longleftrightarrow\quad j_i(x)\in\mathfrak m_i,$$ or the same equivalence holds for the second prescribed embedding $\bar j_i$. Here $\mathfrak m_i$ is the maximal ideal of the twist coefficient DVR, and $j_i,\bar j_i$ take values in its fraction field. The full twist coefficient and character data are those of ([Galois representations and coefficient twists](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NData/)).

Every spectral label $\pi$ in the finite type-label set occurs among the selected or base orthonormal-basis labels: $\pi=\pi_a$ for some selected basis index $a$, or $\pi=\pi^0_a$ for some base basis index $a$.
