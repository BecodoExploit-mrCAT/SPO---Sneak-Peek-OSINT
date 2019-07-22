# -*- coding:UTF-8 -*-
__Author__ = 'Victor de Queiroz'
"""
Class for get json on RECEITA FEDERAL of Brazil
This API is for search data about CNPJ
CNPJ is a Brazilian documentation about companies 

"""
import urllib.request
import json


class CNPJ(object):

    # function for get api
    def getCNPJ(self, cnpj):
        #prepare string
        no = "./-"
        for i in range(0, len(no)):
            cnpj = cnpj.replace(no[i], "")

        #for all data
        try:
            with urllib.request.urlopen("http://compras.dados.gov.br/fornecedores/doc/fornecedor_pj/" + cnpj + ".json") as url:
                 data_not_treated = json.loads(url.read().decode())
        except:
            data_not_treated = { 'error':True }

        
        #treatment of data
        #example of data
        """
        {
            'id_ramo_negocio': 85,
            'complemento_logradouro': None, 
            'caixa_postal': None, 
            'id': 208390, 
            'nome_fantasia': 'COLEGIO OPET', 
            'bairro': 'Rebouças', 
            'id_natureza_juridica': 2, 
            'razao_social': 'OPET ORGANIZACAO PARANAENSE DE ENSINO TECNICO LTDA', 
            'id_cnae': None, 
            'id_unidade_cadastradora': 803090, 
            '_links': {
                'contratos': {'title': 'Contratos deste fornecedor', 
                    'href': '/contratos/v1/contratos?cnpj_contratada=75118406000172'
                }, 
                'porte_empresa': {
                    'title': 'Porte da Empresa 5: 
                    DEMAIS', 
                    'href': '/fornecedores/id/porte_empresa/5'
                }, 
                'ramo_negocio': {
                    'title': 'Ramo de Negócio 85: EDUCAÇÃO', 
                    'href': '/fornecedores/id/ramo_negocio/85'
                }, 
                'municipio': {
                    'title': 'Municipio 75353: Curitiba', 
                    'href': '/fornecedores/id/municipio/75353'
                }, 
                'natureza_juridica': {
                    'title': 'Natureza Jurídica 2: 
                    SOCIEDADE EMPRESÁRIA LIMITADA', 
                    'href': '/fornecedores/id/natureza_juridica/2'
                }, 
                'self': {
                    'title': 'Fornecedor 75.118.406/0001-72: OPET ORGANIZACAO PARANAENSE DE ENSINO TECNICO LTDA', 
                    'href': '/fornecedores/id/fornecedor_pj/75118406000172'
                }, 
                'ocorrencia_fornecedores': {
                    'title': 'Ocorrências aplicadas a este fornecedor', 
                    'href': '/fornecedores/v1/ocorrencias_fornecedores?cnpj=75118406000172'
                }, 
                'licitações': {
                    'title': 'Licitações deste fornecedor', 
                    'href': '/licitacoes/v1/licitacoes?cnpj_vencedor=75118406000172'
                }, 
                'uasg': {
                    'title': 'UASG 803090: SERPRO - REGIONAL CURITIBA', 
                    'href': '/licitacoes/id/uasg/803090'
                }, 
                'linhasFornecimento': {
                    'title': 'Linhas de fornecimento deste fornecedor', 
                    'href': '/fornecedores/v1/linhas_fornecimento?id_fornecedor=208390'
                    }
            },
             
            'ativo': True, 
            'numero_logradouro': None, 
            'habilitado_licitar': True, 
            'recadastrado': False, 
            'cep': '80230-020', 
            'logradouro': 'Avenida iguaçu,755', 
            'id_porte_empresa': 5, 
            'cnpj': '75118406000172', 
            'id_cnae2': None, 
            'id_municipio': 75353
        }

        
        """
        #data treated initalization
        data_treated = {
            'social_name':'',
            'fantasy_name':'',
            'address':'',
            'type_business':'',
            'legal_nature':'',
            'isActive':True,
            'business_size':'',
            'bidding_permission':True,
            'public_contracts':'',
            'biddings':''
        }

        #data treated values
        if 'error' in data_not_treated:
            data_treated['social_name'] = ''
            data_treated['fantasy_name'] =''
            data_treated['address'] = ''
            data_treated['type_business'] =''
            data_treated['legal_nature'] = ''
            data_treated['isActive'] = ''
            data_treated['business_size'] = ''
            data_treated['bidding_permission'] = ''
            data_treated['public_contracts'] = ''
            data_treated['biddings'] = ""
        else:
            data_treated['social_name']=data_not_treated['razao_social']
            data_treated['fantasy_name']=data_not_treated['nome_fantasia']
            data_treated['address']=str(data_not_treated['logradouro'])+" , "+str(data_not_treated['_links']['municipio']['title']).split(": ")[1]+"  "+str(data_not_treated['cep'])
            data_treated['type_business']=str(data_not_treated['_links']['ramo_negocio']['title']).split(": ")[1]
            data_treated['legal_nature']=str(data_not_treated['_links']['natureza_juridica']['title']).split(': ')[1]
            data_treated['isActive']=data_not_treated['ativo']
            data_treated['business_size']=str(data_not_treated['_links']['porte_empresa']['title']).split(": ")[1]
            data_treated['bidding_permission']=data_not_treated['habilitado_licitar']
            if cnpj is None:
                data_treated['public_contracts'] = ""
            else:
                data_treated['public_contracts']="http://compras.dados.gov.br/contratos/v1/contratos?cnpj_contratada="+cnpj
            if cnpj is None:
                data_treated['biddings'] = ""
            else:
                data_treated['biddings']="http://compras.dados.gov.br/licitacoes/v1/licitacoes?cnpj_vencedor="+cnpj



        return data_treated


    def treat(self,cnpj):
        # prepare string
        no = "./-"
        for i in range(0, len(no)):
            cnpj = cnpj.replace(no[i], "")

        return cnpj


