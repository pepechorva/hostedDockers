<?php

    $config['system']['current_config_version']              = 2;
    $config['db']['type']                                    = 'mysql';
    $config['db']['host']                                    = 'serversNET';
    $config['db']['port']                                    = '3306';
    $config['db']['name']                                    = 'partdb';
    $config['db']['user']                                    = 'partdb';
    $config['db']['password']                                = 'PASSWORD';
    $config['db']['charset']                                 = 'utf8';
    $config['db']['auto_update']                             = false;
    $config['db']['backup']['name']                          = '';
    $config['db']['backup']['url']                           = '';
    $config['db']['update_error']['version']                 = -1;
    $config['db']['update_error']['next_step']               = 0;
    $config['db']['limit']['search_parts']                   = 200;
    $config['db']['space_fix']                               = false;
    $config['html']['http_charset']                          = 'utf-8';
    $config['html']['theme']                                 = 'nextgen';
    $config['html']['custom_css']                            = 'slate.css';
    $config['update']['type']                                = 'stable';
    $config['startup']['custom_banner']                      = '';
    $config['startup']['disable_update_list']                = false;
    $config['startup']['disable_search_warning']             = false;
    $config['devices']['disable']                            = false;
    $config['footprints']['disable']                         = false;
    $config['manufacturers']['disable']                      = false;
    $config['auto_datasheets']['disable']                    = false;
    $config['suppliers']['disable']                          = false;
    $config['tools']['footprints']['autoload']               = false;
    $config['menu']['disable_help']                          = false;
    $config['menu']['disable_config']                        = false;
    $config['menu']['enable_debug']                          = false;
    $config['menu']['disable_labels']                        = false;
    $config['menu']['disable_calculator']                    = false;
    $config['menu']['disable_iclogos']                       = false;
    $config['menu']['disable_footprints']                    = false;
    $config['popup']['modal']                                = false;
    $config['popup']['width']                                = 1000;
    $config['popup']['height']                               = 800;
    $config['debug']['enable']                               = false;
    $config['debug']['debugbar']                             = false;
    $config['debug']['debugbar_db']                          = false;
    $config['debug']['template_debugging_enable']            = false;
    $config['debug']['request_debugging_enable']             = false;
    $config['installation_complete']['locales']              = true;
    $config['installation_complete']['admin_password']       = true;
    $config['installation_complete']['database']             = true;
    $config['installation_complete']['db_backup_path']       = true;
    $config['timezone']                                      = 'Europe/Madrid';
    $config['language']                                      = 'en_US';
    $config['is_online_demo']                                = false;
    $config['developer_mode']                                = false;
    $config['page_title']                                    = 'Part-DB Elektronische Bauteile-Datenbank';
    $config['partdb_title']                                  = 'Part-DB';
    $config['tracking_code']                                 = '';
    $config['allow_server_downloads']                        = false;
    $config['design']['use_smarty']                          = true;
    $config['foot3d']['active']                              = true;
    $config['foot3d']['show_info']                           = false;
    $config['appearance']['use_old_datasheet_icons']         = false;
    $config['appearance']['short_description_length']        = 200;
    $config['appearance']['short_description']               = true;
    $config['other_panel']['collapsed']                      = false;
    $config['other_panel']['position']                       = 'top';
    $config['part_info']['hide_actions']                     = true;
    $config['part_info']['hide_empty_attachements']          = false;
    $config['part_info']['hide_empty_orderdetails']          = false;
    $config['properties']['active']                          = false;
    $config['edit_parts']['created_go_to_info']              = true;
    $config['edit_parts']['saved_go_to_info']                = false;
    $config['table']['autosort']                             = false;
    $config['table']['default_show_subcategories']           = true;
    $config['table']['default_limit']                        = 50;
    $config['table']['full_paths']                           = false;
    $config['table']['instock_warning_full_row_color']       = false;
    $config['search']['livesearch']                          = true;
    $config['search']['highlighting']                        = true;
    $config['attachements']['folder_structure']              = true;
    $config['attachements']['download_default']              = false;
    $config['attachements']['show_name']                     = false;
    $config['user']['avatars']['use_gravatar']               = false;
    $config['user']['redirect_to_login']                     = true;
    $config['user']['gc_maxlifetime']                        = '5400';
    $config['cookie_consent']['enable']                      = false;
    $config['cookie_consent']['message']                     = 'This website uses cookies to ensure you get the best experience on our website.';
    $config['cookie_consent']['link_text']                   = 'Learn more';
    $config['cookie_consent']['button_text']                 = 'Got it!';
    $config['cookie_consent']['link_href']                   = 'https://cookiesandyou.com/';
    $config['logging_system']['ip_anonymize_mask_ipv4']      = '255.255.255.0';
    $config['logging_system']['ip_anonymize_mask_ipv6']      = 'ffff:ffff:ffff:ffff:0000:0000:0000:0000';
    $config['logging_system']['min_level']                   = 7;

    //How to declare manual configs:
    //$manual_config['money_format']['POSIX']                = '%!n €';
    //$manual_config['DOCUMENT_ROOT']                        = '/var/www';

