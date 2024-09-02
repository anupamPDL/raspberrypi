from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.decorators import dag, task
import os 
import sys
import requests
import json
import subprocess
import tsslogging
import shutil
from git import Repo

sys.dont_write_bytecode = True

######################################################USER CHOSEN PARAMETERS ###########################################################
default_args = {    
 'conf_project' : 'Transactional Machine Learning (TML)',
 'conf_copyright' : '2024, Otics Advanced Analytics, Incorporated - For Support email support@otics.ca',
 'conf_author' : 'Sebastian Maurice',
 'conf_release' : '0.1',
 'conf_version' : '0.1.0'
}

############################################################### DO NOT MODIFY BELOW ####################################################
# Instantiate your DAG
@dag(dag_id="tml_system_step_10_documentation_dag_myawesometmlsolution5", default_args=default_args, tags=["tml_system_step_10_documentation_dag_myawesometmlsolution5"], schedule=None,  catchup=False)
def startdocumentation():
    # Define tasks
    def empty():
        pass
dag = startdocumentation()

def doparse(fname,farr):
      data = ''
      with open(fname, 'r', encoding='utf-8') as file: 
        data = file.readlines() 
        r=0
        for d in data:        
            for f in farr:
                fs = f.split(";")
                if fs[0] in d:
                    data[r] = d.replace(fs[0],fs[1])
            r += 1  
      with open(fname, 'w', encoding='utf-8') as file: 
        file.writelines(data)
    
def generatedoc(**context):    
    
    if 'tssdoc' in os.environ:
        if os.environ['tssdoc']=="1":
            return
    
    sname = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="solutionname")

    producinghost = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="VIPERHOSTPRODCE")
    producingport = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="VIPERPORTPRODUCE")
    preprocesshost = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="VIPERHOSTPREPROCESS")
    preprocessport = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="VIPERPORTPREPROCESS")
    mlhost = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="VIPERHOSTML")
    mlport = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="VIPERPORTML")
    predictionhost = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="VIPERHOSTPREDICT")
    predictionport = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="VIPERHOSTPREDICT")
    dashboardhtml = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="dashboardhtml")
    
    hpdehost = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="HPDEHOST")
    hpdeport = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="HPDEPORT")

    hpdepredicthost = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="HPDEHOSTPREDICT")
    hpdepredictport = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="HPDEPORTPREDICT")
    
    subprocess.call(["sed", "-i", "-e",  "s/--project--/{}/g".format(default_args['conf_project']), "/{}/docs/source/conf.py".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--copyright--/{}/g".format(default_args['conf_copyright']), "/{}/docs/source/conf.py".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--author--/{}/g".format(default_args['conf_author']), "/{}/docs/source/conf.py".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--release--/{}/g".format(default_args['conf_release']), "/{}/docs/source/conf.py".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--version--/{}/g".format(default_args['conf_version']), "/{}/docs/source/conf.py".format(sname)])
    
    stitle = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="solutiontitle")
    sdesc = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="solutiondescription")
    brokerhost = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="brokerhost")
    brokerport = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="brokerport")
    cloudusername = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="cloudusername")
    cloudpassword = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="cloudpassword")
    ingestdatamethod = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="ingestdatamethod")

    subprocess.call(["sed", "-i", "-e",  "s/--solutionname--/{}/g".format(sname), "/{}/docs/source/index.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--solutiontitle--/{}/g".format(stitle), "/{}/docs/source/index.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--solutiondescription--/{}/g".format(sdesc), "/{}/docs/source/index.rst".format(sname)])

    subprocess.call(["sed", "-i", "-e",  "s/--solutionname--/{}/g".format(sname), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--sname--/{}/g".format(sname), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--stitle--/{}/g".format(stitle), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--sdesc--/{}/g".format(sdesc), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--brokerhost--/{}/g".format(brokerhost), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--brokerport--/{}/g".format(brokerport[1:]), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--cloudusername--/{}/g".format(cloudusername), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--ingestdatamethod--/{}/g".format(ingestdatamethod), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--solutiontitle--/{}/g".format(stitle), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--solutiondescription--/{}/g".format(sdesc), "/{}/docs/source/details.rst".format(sname)])

    
    companyname = context['ti'].xcom_pull(task_ids='step_2_solution_task_createtopic',key="companyname")
    myname = context['ti'].xcom_pull(task_ids='step_2_solution_task_createtopic',key="myname")
    myemail = context['ti'].xcom_pull(task_ids='step_2_solution_task_createtopic',key="myemail")
    mylocation = context['ti'].xcom_pull(task_ids='step_2_solution_task_createtopic',key="mylocation")
    replication = context['ti'].xcom_pull(task_ids='step_2_solution_task_createtopic',key="replication")
    numpartitions = context['ti'].xcom_pull(task_ids='step_2_solution_task_createtopic',key="numpartitions")
    enabletls = context['ti'].xcom_pull(task_ids='step_2_solution_task_createtopic',key="enabletls")
    microserviceid = context['ti'].xcom_pull(task_ids='step_2_solution_task_createtopic',key="microserviceid")
    raw_data_topic = context['ti'].xcom_pull(task_ids='step_2_solution_task_createtopic',key="raw_data_topic")
    preprocess_data_topic = context['ti'].xcom_pull(task_ids='step_2_solution_task_createtopic',key="preprocess_data_topic")
    ml_data_topic = context['ti'].xcom_pull(task_ids='step_2_solution_task_createtopic',key="ml_data_topic")
    prediction_data_topic = context['ti'].xcom_pull(task_ids='step_2_solution_task_createtopic',key="prediction_data_topic")

    subprocess.call(["sed", "-i", "-e",  "s/--companyname--/{}/g".format(companyname), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--myname--/{}/g".format(myname), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--myemail--/{}/g".format(myemail), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--mylocation--/{}/g".format(mylocation), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--replication--/{}/g".format(replication[1:]), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--numpartitions--/{}/g".format(numpartitions[1:]), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--enabletls--/{}/g".format(enabletls[1:]), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--microserviceid--/{}/g".format(microserviceid), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--raw_data_topic--/{}/g".format(raw_data_topic), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--preprocess_data_topic--/{}/g".format(preprocess_data_topic), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--ml_data_topic--/{}/g".format(ml_data_topic), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--prediction_data_topic--/{}/g".format(prediction_data_topic), "/{}/docs/source/details.rst".format(sname)])
    
    PRODUCETYPE = ""  
    TOPIC = ""
    PORT = ""
    IDENTIFIER = ""
    if ingestdatamethod == "localfile":
            PRODUCETYPE = context['ti'].xcom_pull(task_ids='step_3_solution_task_producetotopic',key="PRODUCETYPE")
            TOPIC = context['ti'].xcom_pull(task_ids='step_3_solution_task_producetotopic',key="TOPIC")
            PORT = context['ti'].xcom_pull(task_ids='step_3_solution_task_producetotopic',key="PORT")
            IDENTIFIER = context['ti'].xcom_pull(task_ids='step_3_solution_task_producetotopic',key="IDENTIFIER")   
    elif ingestdatamethod == "mqtt":
            PRODUCETYPE = context['ti'].xcom_pull(task_ids='step_3_solution_task_producetotopic',key="PRODUCETYPE")
            TOPIC = context['ti'].xcom_pull(task_ids='step_3_solution_task_producetotopic',key="TOPIC")
            PORT = context['ti'].xcom_pull(task_ids='step_3_solution_task_producetotopic',key="PORT")
            IDENTIFIER = context['ti'].xcom_pull(task_ids='step_3_solution_task_producetotopic',key="IDENTIFIER")
    elif ingestdatamethod == "rest":
            PRODUCETYPE = context['ti'].xcom_pull(task_ids='step_3_solution_task_producetotopic',key="PRODUCETYPE")
            TOPIC = context['ti'].xcom_pull(task_ids='step_3_solution_task_producetotopic',key="TOPIC")
            PORT = context['ti'].xcom_pull(task_ids='step_3_solution_task_producetotopic',key="PORT")
            IDENTIFIER = context['ti'].xcom_pull(task_ids='step_3_solution_task_producetotopic',key="IDENTIFIER")
    elif ingestdatamethod == "grpc":
            PRODUCETYPE = context['ti'].xcom_pull(task_ids='step_3_solution_task_producetotopic',key="PRODUCETYPE")
            TOPIC = context['ti'].xcom_pull(task_ids='step_3_solution_task_producetotopic',key="TOPIC")
            PORT = context['ti'].xcom_pull(task_ids='step_3_solution_task_producetotopic',key="PORT")
            IDENTIFIER = context['ti'].xcom_pull(task_ids='step_3_solution_task_producetotopic',key="IDENTIFIER")

    subprocess.call(["sed", "-i", "-e",  "s/--PRODUCETYPE--/{}/g".format(PRODUCETYPE), "/{}/docs/source/details.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--TOPIC--/{}/g".format(TOPIC), "/{}/docs/source/details.rst".format(sname)])
    doparse("/{}/docs/source/details.rst".format(sname), ["--PORT--;{}".format(PORT)])
    
    subprocess.call(["sed", "-i", "-e",  "s/--IDENTIFIER--/{}/g".format(IDENTIFIER), "/{}/docs/source/details.rst".format(sname)])
            
    raw_data_topic = context['ti'].xcom_pull(task_ids='step_4_solution_task_preprocess',key="raw_data_topic")
    preprocess_data_topic = context['ti'].xcom_pull(task_ids='step_4_solution_task_preprocess',key="preprocess_data_topic")    
    preprocessconditions = context['ti'].xcom_pull(task_ids='step_4_solution_task_preprocess',key="preprocessconditions")
    delay = context['ti'].xcom_pull(task_ids='step_4_solution_task_preprocess',key="delay")
    array = context['ti'].xcom_pull(task_ids='step_4_solution_task_preprocess',key="array")
    saveasarray = context['ti'].xcom_pull(task_ids='step_4_solution_task_preprocess',key="saveasarray")
    topicid = context['ti'].xcom_pull(task_ids='step_4_solution_task_preprocess',key="topicid")
    rawdataoutput = context['ti'].xcom_pull(task_ids='step_4_solution_task_preprocess',key="rawdataoutput")
    asynctimeout = context['ti'].xcom_pull(task_ids='step_4_solution_task_preprocess',key="asynctimeout")
    timedelay = context['ti'].xcom_pull(task_ids='step_4_solution_task_preprocess',key="timedelay")
    usemysql = context['ti'].xcom_pull(task_ids='step_4_solution_task_preprocess',key="usemysql")
    preprocesstypes = context['ti'].xcom_pull(task_ids='step_4_solution_task_preprocess',key="preprocesstypes")
    pathtotmlattrs = context['ti'].xcom_pull(task_ids='step_4_solution_task_preprocess',key="pathtotmlattrs")
    identifier = context['ti'].xcom_pull(task_ids='step_4_solution_task_preprocess',key="identifier")
    jsoncriteria = context['ti'].xcom_pull(task_ids='step_4_solution_task_preprocess',key="jsoncriteria")

    if preprocess_data_topic:
        subprocess.call(["sed", "-i", "-e",  "s/--raw_data_topic--/{}/g".format(raw_data_topic), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--preprocess_data_topic--/{}/g".format(preprocess_data_topic), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--preprocessconditions--/{}/g".format(preprocessconditions), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--delay--/{}/g".format(delay[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--array--/{}/g".format(array[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--saveasarray--/{}/g".format(saveasarray[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--topicid--/{}/g".format(topicid[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--rawdataoutput--/{}/g".format(rawdataoutput[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--asynctimeout--/{}/g".format(asynctimeout[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--timedelay--/{}/g".format(timedelay[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--preprocesstypes--/{}/g".format(preprocesstypes), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--pathtotmlattrs--/{}/g".format(pathtotmlattrs), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--identifier--/{}/g".format(identifier), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--jsoncriteria--/{}/g".format(jsoncriteria), "/{}/docs/source/details.rst".format(sname)])
    
    preprocess_data_topic = context['ti'].xcom_pull(task_ids='step_5_solution_task_ml',key="preprocess_data_topic")
    ml_data_topic = context['ti'].xcom_pull(task_ids='step_5_solution_task_ml',key="ml_data_topic")
    modelruns = context['ti'].xcom_pull(task_ids='step_5_solution_task_ml',key="modelruns")
    offset = context['ti'].xcom_pull(task_ids='step_5_solution_task_ml',key="offset")
    islogistic = context['ti'].xcom_pull(task_ids='step_5_solution_task_ml',key="islogistic")
    networktimeout = context['ti'].xcom_pull(task_ids='step_5_solution_task_ml',key="networktimeout")
    modelsearchtuner = context['ti'].xcom_pull(task_ids='step_5_solution_task_ml',key="modelsearchtuner")
    dependentvariable = context['ti'].xcom_pull(task_ids='step_5_solution_task_ml',key="dependentvariable")
    independentvariables = context['ti'].xcom_pull(task_ids='step_5_solution_task_ml',key="independentvariables")
    rollbackoffsets = context['ti'].xcom_pull(task_ids='step_5_solution_task_ml',key="rollbackoffsets")
    topicid = context['ti'].xcom_pull(task_ids='step_5_solution_task_ml',key="topicid")
    consumefrom = context['ti'].xcom_pull(task_ids='step_5_solution_task_ml',key="consumefrom")
    fullpathtotrainingdata = context['ti'].xcom_pull(task_ids='step_5_solution_task_ml',key="fullpathtotrainingdata")
    transformtype = context['ti'].xcom_pull(task_ids='step_5_solution_task_ml',key="transformtype")
    sendcoefto = context['ti'].xcom_pull(task_ids='step_5_solution_task_ml',key="sendcoefto")
    coeftoprocess = context['ti'].xcom_pull(task_ids='step_5_solution_task_ml',key="coeftoprocess")
    coefsubtopicnames = context['ti'].xcom_pull(task_ids='step_5_solution_task_ml',key="coefsubtopicnames")

    if modelruns: 
        subprocess.call(["sed", "-i", "-e",  "s/--preprocess_data_topic--/{}/g".format(preprocess_data_topic), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--ml_data_topic--/{}/g".format(ml_data_topic), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--modelruns--/{}/g".format(modelruns[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--offset--/{}/g".format(offset[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--islogistic--/{}/g".format(islogistic[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--networktimeout--/{}/g".format(networktimeout[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--modelsearchtuner--/{}/g".format(modelsearchtuner[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--dependentvariable--/{}/g".format(dependentvariable), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--independentvariables--/{}/g".format(independentvariables), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--rollbackoffsets--/{}/g".format(rollbackoffsets[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--topicid--/{}/g".format(topicid[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--consumefrom--/{}/g".format(consumefrom), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--fullpathtotrainingdata--/{}/g".format(fullpathtotrainingdata), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--transformtype--/{}/g".format(transformtype), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--sendcoefto--/{}/g".format(sendcoefto), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--coeftoprocess--/{}/g".format(coeftoprocess), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--coefsubtopicnames--/{}/g".format(coefsubtopicnames), "/{}/docs/source/details.rst".format(sname)])
    
    preprocess_data_topic = context['ti'].xcom_pull(task_ids='step_6_solution_task_prediction',key="preprocess_data_topic")
    ml_prediction_topic = context['ti'].xcom_pull(task_ids='step_6_solution_task_prediction',key="ml_prediction_topic")
    streamstojoin = context['ti'].xcom_pull(task_ids='step_6_solution_task_prediction',key="streamstojoin")
    inputdata = context['ti'].xcom_pull(task_ids='step_6_solution_task_prediction',key="inputdata")
    consumefrom = context['ti'].xcom_pull(task_ids='step_6_solution_task_prediction',key="consumefrom")
    offset = context['ti'].xcom_pull(task_ids='step_6_solution_task_prediction',key="offset")
    delay = context['ti'].xcom_pull(task_ids='step_6_solution_task_prediction',key="delay")
    usedeploy = context['ti'].xcom_pull(task_ids='step_6_solution_task_prediction',key="usedeploy")
    networktimeout = context['ti'].xcom_pull(task_ids='step_6_solution_task_prediction',key="networktimeout")
    maxrows = context['ti'].xcom_pull(task_ids='step_6_solution_task_prediction',key="maxrows")
    topicid = context['ti'].xcom_pull(task_ids='step_6_solution_task_prediction',key="topicid")
    pathtoalgos = context['ti'].xcom_pull(task_ids='step_6_solution_task_prediction',key="pathtoalgos")

    if ml_prediction_topic:
        subprocess.call(["sed", "-i", "-e",  "s/--preprocess_data_topic--/{}/g".format(preprocess_data_topic), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--ml_prediction_topic--/{}/g".format(ml_prediction_topic), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--streamstojoin--/{}/g".format(streamstojoin), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--inputdata--/{}/g".format(inputdata), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--consumefrom--/{}/g".format(consumefrom), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--offset--/{}/g".format(offset[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--delay--/{}/g".format(delay[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--usedeploy--/{}/g".format(usedeploy[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--networktimeout--/{}/g".format(networktimeout[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--maxrows--/{}/g".format(maxrows[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--topicid--/{}/g".format(topicid[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--pathtoalgos--/{}/g".format(pathtoalgos), "/{}/docs/source/details.rst".format(sname)])

    
    vipervizport = context['ti'].xcom_pull(task_ids='step_7_solution_task_visualization',key="VIPERVIZPORT")
    topic = context['ti'].xcom_pull(task_ids='step_7_solution_task_visualization',key="topic")
    secure = context['ti'].xcom_pull(task_ids='step_7_solution_task_visualization',key="secure")
    offset = context['ti'].xcom_pull(task_ids='step_7_solution_task_visualization',key="offset")
    append = context['ti'].xcom_pull(task_ids='step_7_solution_task_visualization',key="append")
    chip = context['ti'].xcom_pull(task_ids='step_7_solution_task_visualization',key="chip")
    rollbackoffset = context['ti'].xcom_pull(task_ids='step_7_solution_task_visualization',key="rollbackoffset")

    containername = context['ti'].xcom_pull(task_ids='step_8_solution_task_containerize',key="containername")
    if containername:
        hcname = containername.split('/')[1]
        huser = containername.split('/')[0]
        hurl = "https://hub.docker.com/r/{}/{}".format(huser,hcname)
    else:    
        containername="TBD"
    
    if vipervizport:
        subprocess.call(["sed", "-i", "-e",  "s/--vipervizport--/{}/g".format(vipervizport[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--topic--/{}/g".format(topic), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--secure--/{}/g".format(secure[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--offset--/{}/g".format(offset[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--append--/{}/g".format(append[1:]), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--chip--/{}/g".format(chip), "/{}/docs/source/details.rst".format(sname)])
        subprocess.call(["sed", "-i", "-e",  "s/--rollbackoffset--/{}/g".format(rollbackoffset[1:]), "/{}/docs/source/details.rst".format(sname)])

    airflowport = tsslogging.getfreeport()
    
    repo = tsslogging.getrepo() 
    gitrepo="https://github.com/{}/{}/tree/main/tml-airflow/dags/tml-solutions/{}".format(os.environ['GITUSERNAME'],repo,sname)
   # gitrepo = "\/{}\/tml-airflow\/dags\/tml-solutions\/{}".format(repo,sname)
    
    v=subprocess.call(["sed", "-i", "-e",  "s/--gitrepo--/{}/g".format(gitrepo), "/{}/docs/source/operating.rst".format(sname)])
    print("V=",v)
    doparse("/{}/docs/source/operating.rst".format(sname), ["--gitrepo--;{}".format(gitrepo)])
    
    subprocess.call(["sed", "-i", "-e",  "s/--solutionname--/{}/g".format(sname), "/{}/docs/source/operating.rst".format(sname)])
    subprocess.call(["sed", "-i", "-e",  "s/--dockercontainer--/{}\n\n{}/g".format(containername,hurl), "/{}/docs/source/operating.rst".format(sname)])
       
    dockerrun = ("docker run -d --net=host --env TSS=0 --env SOLUTIONNAME=TSS --env AIRFLOWPORT={} --env GITUSERNAME={} " \
                 "--env GITPASSWORD=<Enter Github Password>  --env GITREPOURL={} --env AIRFLOWPORT=<TBD At Runtime> " \
                 "--env READTHEDOCS=<Enter Readthedocs token> {}" \
                 .format(airflowport,os.environ['GITUSERNAME'],os.environ['GITREPOURL'],containername))   
    
   # dockerrun = re.escape(dockerrun) 
    v=subprocess.call(["sed", "-i", "-e",  "s/--dockerrun--/{}/g".format(dockerrun), "/{}/docs/source/operating.rst".format(sname)])
   

    doparse("/{}/docs/source/operating.rst".format(sname), ["--dockerrun--;{}".format(dockerrun),"--dockercontainer--;{} ({})".format(containername, hurl)])
    doparse("/{}/docs/source/details.rst".format(sname), ["--dockerrun--;{}".format(dockerrun),"--dockercontainer--;{} ({})".format(containername, hurl)])
    
    privategptcontainer = "https://hub.docker.com/r/maadsdocker/tml-privategpt-with-gpu-nvidia-amd64"
    privategptrun = "docker run -d -p 8001:8001 --gpus all --net=host --env PORT=8001 --env GPU=1 --env WEB_CONCURRENCY=1 --env COLLECTION=tml-cisco --env CUDA_VISIBLE_DEVICES=0 maadsdocker/tml-privategpt-with-gpu-nvidia-amd64"
    doparse("/{}/docs/source/details.rst".format(sname), ["--privategptcontainer--;{}".format(privategptcontainer),"--privategptrun--;{}".format(privategptrun)])

    qdrantcontainer = "qdrant/qdrant"
    qdrantrun = "docker run -d -p 6333:6333 -v $(pwd)/qdrant_storage:/qdrant/storage:z qdrant/qdrant"
    doparse("/{}/docs/source/details.rst".format(sname), ["--qdrantcontainer--;{}".format(qdrantcontainer),"--qdrantrun--;{}".format(qdrantrun)])

    rbuf = "https://{}.readthedocs.io".format(sname)
    doparse("/{}/docs/source/details.rst".format(sname), ["--readthedocs--;{}".format(rbuf)])
    
    vizurl = "http:\/\/localhost:{}\/{}?topic={}\&offset={}\&groupid=\&rollbackoffset={}\&topictype=prediction\&append={}\&secure={}".format(vipervizport[1:],dashboardhtml,topic,offset[1:],rollbackoffset[1:],append[1:],secure[1:])
    subprocess.call(["sed", "-i", "-e",  "s/--visualizationurl--/{}/g".format(vizurl), "/{}/docs/source/operating.rst".format(sname)])


    airflowurl = "http:\/\/localhost:{}".format(airflowport)
    subprocess.call(["sed", "-i", "-e",  "s/--airflowurl--/{}/g".format(airflowurl), "/{}/docs/source/operating.rst".format(sname)])
    
    readthedocs = "https:\/\/{}.readthedocs.io".format(sname)
    subprocess.call(["sed", "-i", "-e",  "s/--readthedocs--/{}/g".format(readthedocs), "/{}/docs/source/operating.rst".format(sname)])
    
    triggername = context['ti'].xcom_pull(task_ids='step_8_solution_task_containerize',key="solution_dag_to_trigger")
    print("triggername=",triggername)
    doparse("/{}/docs/source/operating.rst".format(sname), ["--triggername--;{}".format(triggername)])

    producinghost = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="VIPERHOSTPRODUCE")
    producingport = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="VIPERPORTPRODUCE")
    preprocesshost = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="VIPERHOSTPREPROCESS")
    preprocessport = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="VIPERPORTPREPROCESS")
    mlhost = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="VIPERHOSTML")
    mlport = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="VIPERPORTML")
    predictionhost = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="VIPERHOSTPREDICT")
    predictionport = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="VIPERPORTPREDICT")

    hpdehost = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="HPDEHOST")
    hpdeport = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="HPDEPORT")

    hpdepredicthost = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="HPDEHOSTPREDICT")
    hpdepredictport = context['ti'].xcom_pull(task_ids='step_1_solution_task_getparams',key="HPDEPORTPREDICT")
        
    tmlbinaries = ("VIPERHOST_PRODUCE={}, VIPERPORT_PRODUCE={}, "
                       "VIPERHOST_PREPOCESS={}, VIPERPORT_PREPROCESS={}, "
                       "VIPERHOST_ML={}, VIPERPORT_ML={}, "
                       "VIPERHOST_PREDCT={}, VIPERPORT_PREDICT={}, "
                       "HPDEHOST={}, HPDEPORT={}, "
                       "HPDEHOST_PREDICT={}, HPDEPORT_PREDICT={}".format(producinghost,producingport[1:],preprocesshost,preprocessport[1:],
                                                                              mlhost,mlport[1:],predictionhost,predictionport[1:],
                                                                              hpdehost,hpdeport[1:],hpdepredicthost,hpdepredictport[1:] ))
    print("TML=",tmlbinaries)
    
    subprocess.call(["sed", "-i", "-e",  "s/--tmlbinaries--/{}/g".format(tmlbinaries), "/{}/docs/source/operating.rst".format(sname)])
    
    with open("/tmux/pythonwindows_{}.txt".format(sname), 'r', encoding='utf-8') as file: 
        data = file.readlines() 
        data.append("viper-produce")
        data.append("viper-preprocess")
        data.append("viper-ml")
        data.append("viper-predict")
        tmuxwindows = ", ".join(data)
        tmuxwindows = tmuxwindows.replace("\n","")
        print("tmuxwindows=",tmuxwindows)

    doparse("/{}/docs/source/operating.rst".format(sname), ["--tmuxwindows--;{}".format(tmuxwindows)])
        
    # Kick off shell script 
    #tsslogging.git_push("/{}".format(sname),"For solution details GOTO: https://{}.readthedocs.io".format(sname),sname)
    os.chdir("/{}".format(repo))
    subprocess.call("git push -f origin main", shell=True)
    
    rtd = context['ti'].xcom_pull(task_ids='step_10_solution_task_document',key="RTD")

    if rtd == None: 
        URL = 'https://readthedocs.org/api/v3/projects/'
        TOKEN = os.environ['READTHEDOCS']
        HEADERS = {'Authorization': f'token {TOKEN}'}
        data={
            "name": "{}".format(sname),
            "repository": {
                "url": "https://github.com/{}/{}".format(os.environ['GITUSERNAME'],sname),
                "type": "git"
            },
            "homepage": "http://template.readthedocs.io/",
            "programming_language": "py",
            "language": "en",
            "privacy_level": "public",
            "external_builds_privacy_level": "public",
            "tags": [
                "automation",
                "sphinx"
            ]
        }
        response = requests.post(
            URL,
            json=data,
            headers=HEADERS,
        )
        print(response.json())
        tsslogging.tsslogit(response.json())
        os.environ['tssdoc']="1"

    ti = context['task_instance']
    ti.xcom_push(key="RTD", value="DONE")
