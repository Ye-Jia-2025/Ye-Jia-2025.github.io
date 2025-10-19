"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views  # 导入 app 的视图模块
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse  # 确保这行存在


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # 注销
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.home, name='home'),  # 将根路径映射到主界面视图
    path('', views.real_home, name='real_home'),
    path('upload-file/', views.upload_file, name='upload_file'),
    path('process-file/', views.process_file, name='process-file'),
    path('send_sms_code/', views.send_sms_code, name='send_sms_code'),
    path('reset_password/', views.reset_password_view, name='reset_password'),
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('index/', views.index, name='index'),#25.04.05  14：33增加成功案例
    # path('chuti/', views.chuti, name='chuti'),  # 关键 name 参数
    path('index2/', views.index2, name='index2'),#25.04.15  08：25增加智能低空平台

    path('chinese_ai/', views.chinese_ai, name='chinese_ai'),  #代码
    path('math_ai/', views.math_ai, name='math_ai'),
    path('english_ai/', views.english_ai, name='english_ai'),
    path('physics_knowledge/', views.physics_knowledge, name='physics_knowledge'),
    path('chemistry_knowledge/', views.chemistry_knowledge, name='chemistry_knowledge'),
    path('biology_knowledge/', views.biology_knowledge, name='biology_knowledge'),
    path('chat_page/', views.chat_page, name='chat_page'),
    path('chinese_knowledge/', views.chinese_knowledge, name='chinese_knowledge'),
    path('homework_correction/', views.homework_correction, name='homework_correction'),
    path('homework_qa/', views.homework_qa, name='homework_qa'),
    path('history_ai/', views.history_ai, name='history_ai'),
    path('geography_ai/', views.geography_ai, name='geography_ai'),
   
    path('math_knowledge/', views.math_knowledge, name='math_knowledge'),
    path('english_knowledge/', views.english_knowledge, name='english_knowledge'),
    path('physics_ai/', views.physics_ai, name='physics_ai'),
    path('chemistry_ai/', views.chemistry_ai, name='chemistry_ai'),
    path('biology_ai/', views.biology_ai, name='biology_ai'),




    path('YJ/', views.YJ, name='YJ'),

    # 课堂智能体相关路径
    path('lab_guidance/', views.lab_guidance, name='lab_guidance'),
    path('science_animation/', views.science_animation, name='science_animation'),
    
    # 历史和地理知识库路径
    path('history_knowledge/', views.history_knowledge, name='history_knowledge'),
    path('geography_knowledge/', views.geography_knowledge, name='geography_knowledge'),

#到这里
    path('anf/', views.anf, name='anf'),
    path('city/', views.city, name='city'),
    path('flfd/', views.flfd, name='flfd'),
    path('ggkz/', views.ggkz, name='ggkz'),
    path('hupo/', views.hupo, name='hupo'),
    path('jc/', views.jc, name='jc'),
    path('jt/', views.jt, name='jt'),
    path('ky/', views.ky, name='ky'),
    path('lvhua/', views.lvhua, name='lvhua'),  #见证奇迹
    path('ly/', views.ly, name='ly'),
    path('nongye/', views.nongye, name='nongye'),
    path('wuliu/', views.wuliu, name='wuliu'),
    path('xhd/', views.xhd, name='xhd'),
    path('ycjy/', views.ycjy, name='ycjy'),
     path('keyan/', views.keyan, name='keyan'),
    # path('yiliao/', views.yiliao, name='yiliao'),


    # 诊前智能体
    # path('symptom_checker/', views.symptom_checker, name='symptom_checker'),
    # path('risk_assessment/', views.risk_assessment, name='risk_assessment'),
    # path('triage_assistant/', views.triage_assistant, name='triage_assistant'),
    # path('anamnesis_recorder/', views.anamnesis_recorder, name='anamnesis_recorder'),
    # path('imaging_preanalysis/', views.imaging_preanalysis, name='imaging_preanalysis'),
    # path('lab_interpreter/', views.lab_interpreter, name='lab_interpreter'),
    # path('telemedicine_assistant/', views.telemedicine_assistant, name='telemedicine_assistant'),
    # path('literature_search/', views.literature_search, name='literature_search'),

    # 诊中智能体
    # path('diagnosis_support/', views.diagnosis_support, name='diagnosis_support'),
    # path('differential_diagnosis/', views.differential_diagnosis, name='differential_diagnosis'),
    # path('treatment_recommendation/', views.treatment_recommendation, name='treatment_recommendation'),
    # path('drug_interaction_checker/', views.drug_interaction_checker, name='drug_interaction_checker'),
    # path('dosage_calculator/', views.dosage_calculator, name='dosage_calculator'),
    # path('clinical_decision_support/', views.clinical_decision_support, name='clinical_decision_support'),
    # path('ai_stethoscope/', views.ai_stethoscope, name='ai_stethoscope'),
    # path('ekg_analysis/', views.ekg_analysis, name='ekg_analysis'),

    # # 诊后智能体
    # path('rehabilitation_plan/', views.rehabilitation_plan, name='rehabilitation_plan'),
    # path('followup_reminder/', views.followup_reminder, name='followup_reminder'),
    # path('medication_adherence/', views.medication_adherence, name='medication_adherence'),
    # path('symptom_monitoring/', views.symptom_monitoring, name='symptom_monitoring'),
    # path('patient_education/', views.patient_education, name='patient_education'),
    # path('chronic_management/', views.chronic_management, name='chronic_management'),
    # path('nutrition_advisor/', views.nutrition_advisor, name='nutrition_advisor'),
    # path('mental_health_support/', views.mental_health_support, name='mental_health_support'),

    # 其他智能体
    # path('resource_management/', views.resource_management, name='resource_management'),
    # path('scheduling_assistant/', views.scheduling_assistant, name='scheduling_assistant'),
    # path('billing_assistant/', views.billing_assistant, name='billing_assistant'),
    # path('transcription_assistant/', views.transcription_assistant, name='transcription_assistant'),
    # path('compliance_monitor/', views.compliance_monitor, name='compliance_monitor'),
    # path('epidemiology_tracker/', views.epidemiology_tracker, name='epidemiology_tracker'),
    # path('medical_translation/', views.medical_translation, name='medical_translation'),
    # path('health_data_analytics/', views.health_data_analytics, name='health_data_analytics'),

    # path('categories_2/', views.my_categories_view_2, name='categories_2'),
    # path('categories_3/', views.my_categories_view_3, name='categories_3'),
    # path('categories_4/', views.my_categories_view_4, name='categories_4'),
    # path('get_tasks/', views.get_tasks, name='get_tasks'),
    # path('generate_course/', views.generate_course, name='generate_course'),
    # path('get_finished_tasks/', views.get_finished_tasks, name='get_finished_tasks'),
    # path('generate_script/', views.generate_script, name='generate_script'),
    # path('delete_task/', views.delete_task, name='delete_task'),
    # path('download_script/', views.download_script, name='download_script'),

    # path('wenti/', views.wenti, name='wenti'),  #0612
    path('wenzi/', views.wenzi, name='wenzi'),  #0706



    path("pay/native/", views.create_native_order, name="wechat_native"),
    path("pay/notify/", views.wechat_notify, name="wechat_notify"),
    path("pay/query/",  views.query_order_status, name="wechat_query"),
    path('pay/subscribe/', views.pay_discription, name='pay_discription'),
    
    path('get_conversations/', views.get_conversations, name='get_conversations'),
    path('create_conversation/', views.create_conversation, name='create_conversation'),
    path('send_message/', views.send_message, name='send_message'),
    path('send_message_stream/', views.send_message_stream, name='send_message_stream'),  # 新增流式API端点
    path('delete_conversation/', views.delete_conversation, name='delete_conversation'),
    path('upload_chat_file/', views.upload_chat_file, name='upload_chat_file'),
    path('page_loca/', views.page_loca, name='page_loca'),
    path('upload_local_file/', views.upload_local_file, name='upload_local_file'),
    path('list_local_files/', views.list_local_files, name='list_local_files'),
    path('delete_local_file/', views.delete_local_file, name='delete_local_file'),
    path('page_loca/', views.page_loca, name='page_loca'),
    path('update_local_file_activation/', views.update_local_file_activation, name='update_local_file_activation'),
    path('check_file_processing_status/', views.check_file_processing_status, name='check_file_processing_status'),
    path('reprocess_file/', views.reprocess_file, name='reprocess_file'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('check_status/', views.check_status, name='check_status'),
    path('categories/', views.my_categories_view, name='categories'),
    path('categories_2/', views.my_categories_view_2, name='categories_2'),
    path('categories_3/', views.my_categories_view_3, name='categories_3'),
    path('categories_4/', views.my_categories_view_4, name='categories_4'),
    path('get_tasks/', views.get_tasks, name='get_tasks'),
    path('generate_course/', views.generate_course, name='generate_course'),
    path('get_finished_tasks/', views.get_finished_tasks, name='get_finished_tasks'),
    path('generate_script/', views.generate_script, name='generate_script'),
    path('delete_task/', views.delete_task, name='delete_task'),
    path('download_script/', views.download_script, name='download_script'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

