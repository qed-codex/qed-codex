---
{
  "module": "src/Formalism/LocalToGlobal/HermitianForms/BothSym.lean",
  "declarations": [
    "Formalism.L2.Forms.ColsTiedSym"
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

## Symmetric finite levels and column identifications

[Definition / hypothesis ARAK.D164](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.FormsTiedSym/)

Use ([Hermitian column levels and local modifications](https://andrewodesky.com/rh/lean/Formalism.L2.Herm.HermColsCh/)), ([Coordinate lattices and adelic column values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.AtTTied/)) and ([Terminal column lattices and period values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.ClsPTied/)), with the same arithmetic member data. A branch is a fibre of the prescribed finite class-label map. Put $s=m/2-1$ and $r=k+2s+1=k+m-1$. All indices below are zero-based.

For $n\ge0$ define a subgroup $J_n^\epsilon(\kappa)$ of $\mathrm{GL}_n(\kappa)$ as follows. Set $$p(x)=\begin{cases}s+x,&x<k,\\x-k,&k\le x<k+s,\\x,&\text{otherwise},\end{cases}\qquad l(x)=\begin{cases}p(x),&x<r,\\r+\lfloor(x-r)/t\rfloor,&x\ge r.\end{cases}$$ Both $M$ and $M^{-1}$ must satisfy $$M_{xy}=0\quad(l(y)<l(x)),\qquad M_{xx}=1\quad(x<r),\qquad M_{x,k+s}=0\quad(x<k).$$ If $\epsilon$ is true, their final row and final column are those of $I$. For the residue characters of ([Coordinate lattices and adelic column values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.AtTTied/)) put $$\Lambda_b(M)=L_{r,t,b,k}(M).$$ Thus its additive character uses the superdiagonal entries below index $r$ except the entry ending at index $k$, and its multiplicative factors are the determinants of the $b$ successive $t$-blocks beginning at $r$, with entries outside the matrix set to zero.

Hypothesis (symmetric coordinate columns). At every source choose the prime-$T$ coordinate residue data, and choose split local data with both $\pi_{g,a}\in E_0$, as in ([Coordinate lattices and adelic column values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.AtTTied/)). At endpoints $i=0,m$ choose the complete coordinate class, value, rational, integral, metric, local-functional and raising/lowering/dilation conditions of that title. Initially the explicit finite level has parameters $$(a_0,t,b,s,c,z)=(k,t,0,k,k,\mathrm{false}).$$ At $i=m$ use the general finite-level specification with subgroup $J_{N_m}^{\mathrm{true}}(\kappa_v)$ and a chosen character equal to $\Lambda_m$.

For every intermediate $1\le i\le m-1$ and branch $\beta$, choose its complete coordinate class presentation and level from ([Coordinate lattices and adelic column values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.AtTTied/)). Choose finite matrix subgroups $H_{i,\beta,a,v}$ and characters $\lambda_{i,\beta,a,v}$, and require the general finite-level specification for them. Identify the value set of the entire stage with its complex frame tuples. Require the matrix $C$ and determinant-factor identity, the form-space and rational-image characterizations, the local integral criterion at every coefficient place, the classwise normalized Fock pairing, the embedding-dependent majorant norm identity and the branch-preserving dilation conditions of that title.

Choose the ten local-reduction conditions of ([Coordinate lattices and adelic column values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.AtTTied/)) at every $i\le m$, including intermediate stages. At every intermediate stage also choose a family of these reductions used with its branch levels, together with additive equivalences from the branch local modules to the member finite fields. These branch reductions satisfy the local-functional comparison, the branch-preserving raising and lowering formulas, and the mixed-basis criterion for $B_{w,v}$. The endpoint reductions satisfy the corresponding endpoint conditions. These are designated choices of maps; the identifications below specify which of them agree.

At stage $m-1$ choose a common coordinate level of parameter $T_u$ and the general finite-level specification with subgroup $J_{N_{m-1}}^{\mathrm{false}}(\kappa_v)$ and character equal to $\Lambda_{m-1}$. Choose a finite set $Y_b$ with an action of this common adelic level and points $y_\beta$ indexed by branches. Every point of $Y_b$ lies in the orbit of exactly one $y_\beta$. Every branch has the same base lattice as the common level, its adelic subgroup is contained in the common one and is precisely the stabilizer of $y_\beta$, and its character is the restriction of the common character.

Choose every secondary class/value/lattice/majorant, terminal extension, local-functional, frame-extension, evaluation and period condition of ([Terminal column lattices and period values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.ClsPTied/)). Its secondary finite level uses $J_{N_m-1}^{\mathrm{false}}(\kappa_v)$ with character equal to $\Lambda_m$. The recorded determinant discriminant constant is the same at every source, equal to its value at $u_0$.

Hypothesis (Hermitian-coordinate identifications). Choose the same Hermitian levels and local modifications as in ([Hermitian column levels and local modifications](https://andrewodesky.com/rh/lean/Formalism.L2.Herm.HermColsCh/)). At every source the coordinate and Hermitian finite-prime bijections, $\pi_u$ and residue ring maps are equal. Initially, at every intermediate branch, at the unique terminal branch and on $X'$, the following five data agree after the fixed dimension reindexing: base lattice, every local level, adelic level, class representative and stabilizer matrix. On $X'$ this uses the fixed reference base lattice and its secondary levels. Every coordinate secondary class lattice is the fixed-frame image of its Hermitian secondary lattice.

At every $i\le m$, the all-stage coordinate dual-lattice reductions and kernel-lattice reductions agree with the Hermitian ones on corresponding vectors. At intermediate stages the branch dual-lattice reductions also agree with the Hermitian ones. The coordinate $z_0$ and tilting matrices are the fixed-frame images of the Hermitian $z_0$ and isometries. The local split ring isomorphisms, the two $\pi_g$ and initial local frames agree with their initial Hermitian choices.

The entire local split and character datum is independent of the source. The initial local frames and the secondary $X'$ local frames are also independent of the source. For every $a=0,1$ and $v\mid g_a$, the characters $\chi_{a,v,j}$, $0\le j<m$, are pairwise distinct. Their values on every integer are independent of $v$ over fixed $g_a$. There exists a multiplicative character $\omega_a$ of $\mathbb Z/g_a\mathbb Z$ of order $g_a-1$ such that $$\chi_{a,v,j}(b\bmod v)=\omega_a^{2(j+1)}(b\bmod g_a)\qquad(b\in\mathbb Z,\ 0\le j<m).$$
