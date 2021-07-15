rename_vocab_resp <- function(ans_df) {
  df_out <- ans_df %>%
    dplyr::rename(., def_mumble = "Q10") %>%
    dplyr::rename(., def_perspire = "Q11") %>%
    dplyr::rename(., def_gush = "Q12") %>%
    dplyr::rename(., def_massive = "Q13") %>%
    dplyr::rename(., def_feign = "Q14") %>%
    dplyr::rename(., def_unwary = "Q15") %>%
    dplyr::rename(., def_veer = "Q16") %>%
    dplyr::rename(., def_orthodox = "Q17") %>%
    dplyr::rename(., def_stripling = "Q18") %>%
    dplyr::rename(., def_salubrious = "Q19") %>%
    dplyr::rename(., def_limpid = "Q20") %>%
    dplyr::rename(., def_procreate = "Q21") %>%
    dplyr::rename(., def_replete = "Q22") %>%
    dplyr::rename(., def_frieze = "Q23") %>%
    dplyr::rename(., def_treacle = "Q24") %>%
    dplyr::rename(., def_ignominious = "Q25") %>%
    dplyr::rename(., def_abjure = "Q26") %>%
    dplyr::rename(., def_duress = "Q27") %>%
    dplyr::rename(., def_bayonet = "Q29") %>%
    dplyr::rename(., def_astound = "Q30") %>%
    dplyr::rename(., def_contamination = "Q31") %>%
    dplyr::rename(., def_amplify = "Q32") %>%
    dplyr::rename(., def_mural = "Q33") %>%
    dplyr::rename(., def_hale = "Q34") %>%
    dplyr::rename(., def_meander = "Q35") %>%
    dplyr::rename(., def_burnish = "Q36") %>%
    dplyr::rename(., def_duplicity = "Q37") %>%
    dplyr::rename(., def_mundane = "Q38") %>%
    dplyr::rename(., def_deleterious = "Q39") %>%
    dplyr::rename(., def_nascent = "Q40") %>%
    dplyr::rename(., def_prolific = "Q41") %>%
    dplyr::rename(., def_paroxysm = "Q42") %>%
    dplyr::rename(., def_antipodal = "Q43") %>%
    dplyr::rename(., def_acrimony = "Q44") %>%
    dplyr::rename(., def_lissome = "Q45") %>%
    dplyr::rename(., def_succinct = "Q46")
  df_out
}

# This is not right. The correct answer is buried in the data structure.
add_vocab_answers <- function(ans_df, quest_df) {
  ans_df <- ans_df %>%
    dplyr::mutate(., ans_mumble = quest_df$question[quest_df$qid == "QID10"]) %>%
    dplyr::mutate(., ans_perspire = quest_df$question[quest_df$qid == "QID11"]) %>%
    dplyr::mutate(., ans_gush = quest_df$question[quest_df$qid == "QID12"]) %>%
    dplyr::mutate(., ans_massive = quest_df$question[quest_df$qid == "QID13"]) %>%
    dplyr::mutate(., ans_feign = quest_df$question[quest_df$qid == "QID14"]) %>%
    dplyr::mutate(., ans_unwary = quest_df$question[quest_df$qid == "QID15"]) %>%
    dplyr::mutate(., ans_veer = quest_df$question[quest_df$qid == "QID16"]) %>%
    dplyr::mutate(., ans_orthodox = quest_df$question[quest_df$qid == "QID17"]) %>%
    dplyr::mutate(., ans_stripling = quest_df$question[quest_df$qid == "QID18"]) %>%
    dplyr::mutate(., ans_salubrious = quest_df$question[quest_df$qid == "QID19"]) %>%
    dplyr::mutate(., ans_limpid = quest_df$question[quest_df$qid == "QID20"]) %>%
    dplyr::mutate(., ans_procreate = quest_df$question[quest_df$qid == "QID21"]) %>%
    dplyr::mutate(., ans_replete = quest_df$question[quest_df$qid == "QID22"]) %>%
    dplyr::mutate(., ans_frieze = quest_df$question[quest_df$qid == "QID23"]) %>%
    dplyr::mutate(., ans_treacle = quest_df$question[quest_df$qid == "QID24"]) %>%
    dplyr::mutate(., ans_ignominious = quest_df$question[quest_df$qid == "QID25"]) %>%
    dplyr::mutate(., ans_abjure = quest_df$question[quest_df$qid == "QID26"]) %>%
    dplyr::mutate(., ans_duress = quest_df$question[quest_df$qid == "QID27"]) %>%
    dplyr::mutate(., ans_bayonet = quest_df$question[quest_df$qid == "QID29"]) %>%
    dplyr::mutate(., ans_astound = quest_df$question[quest_df$qid == "QID30"]) %>%
    dplyr::mutate(., ans_contamination = quest_df$question[quest_df$qid == "QID31"]) %>%
    dplyr::mutate(., ans_amplify = quest_df$question[quest_df$qid == "QID32"]) %>%
    dplyr::mutate(., ans_mural = quest_df$question[quest_df$qid == "QID33"]) %>%
    dplyr::mutate(., ans_hale = quest_df$question[quest_df$qid == "QID34"]) %>%
    dplyr::mutate(., ans_meander = quest_df$question[quest_df$qid == "QID35"]) %>%
    dplyr::mutate(., ans_burnish = quest_df$question[quest_df$qid == "QID36"]) %>%
    dplyr::mutate(., ans_duplicity = quest_df$question[quest_df$qid == "QID37"]) %>%
    dplyr::mutate(., ans_mundane = quest_df$question[quest_df$qid == "QID38"]) %>%
    dplyr::mutate(., ans_deleterious = quest_df$question[quest_df$qid == "QID39"]) %>%
    dplyr::mutate(., ans_nascent = quest_df$question[quest_df$qid == "QID40"]) %>%
    dplyr::mutate(., ans_prolific = quest_df$question[quest_df$qid == "QID41"]) %>%
    dplyr::mutate(., ans_paroxysm = quest_df$question[quest_df$qid == "QID42"]) %>%
    dplyr::mutate(., ans_antipodal = quest_df$question[quest_df$qid == "QID43"]) %>%
    dplyr::mutate(., ans_acrimony = quest_df$question[quest_df$qid == "QID44"]) %>%
    dplyr::mutate(., ans_lissome = quest_df$question[quest_df$qid == "QID45"]) %>%
    dplyr::mutate(., ans_succinct = quest_df$question[quest_df$qid == "QID45"])
  ans_df
}

extract_vocab <- function(ans_df, quest_df) {
  df_out <- rename_vocab_resp(ans_df)
  df_out <- add_vocab_answers(df_out, quest_df)
  dplyr::select(df_out, `Participant ID`,
                def_mumble, ans_mumble,
                def_perspire, ans_perspire,
                def_gush, ans_gush,
                def_massive, ans_massive,
                def_feign, ans_feign)
}
