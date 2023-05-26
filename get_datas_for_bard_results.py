from bardapi import Bard


def get_bard_result(job_desc,crawl_data):

    token = 'WwgItrGwFRBt2xx-FSLEPMAZGz04Bgt-D-qZQw7P3PZTtX62gTp4Ml_QBWQ72xsiu52pUw.'
    bard = Bard(token=token,timeout=30)
    
    #text = "Can you rate the cv and job description out of a hundred based on the match rate?"
    text = "What is the match rate between Job and CV. Can you tell me how many matches there are using the Jaccard algorithm?"
    #Todo şu algoritmaya göre rate sonuçu kaç çıkar
    response = bard.get_answer(f"Cv:{crawl_data['text']} \n Job Description:{job_desc} \n {text}")['content']

    return response