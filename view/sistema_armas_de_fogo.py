def sistema_mira(sist_causar_dano, local_corpo):
    local = ''
    buff_mira = 0
    debuff_mira = 0

    if sist_causar_dano.toggle("Mirar"):
        sist_causar_dano.write("Mirar em um local especifico do corpo da um debuff de - 4")
        if sist_causar_dano.toggle("Local especifico"):
            local = sist_causar_dano.selectbox("Local mirado", local_corpo)
            debuff_mira = 4
        else:
            sist_causar_dano.write("Mira da um buff de ate 3 na precisão")
            turnos_mirando = sist_causar_dano.number_input("Turnos mirando", min_value=1)

            if turnos_mirando > 3:
                buff_mira = 3
            else:
                buff_mira = turnos_mirando
    return buff_mira, debuff_mira, local

