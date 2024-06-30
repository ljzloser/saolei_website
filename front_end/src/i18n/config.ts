import type { VueMessageType } from 'vue-i18n'
import { LocaleMessage } from '@intlify/core-base'

/**
 * 配置语法：https://vue-i18n.intlify.dev/guide/essentials/syntax.html
 */
export type LocaleConfig = LocaleMessage<VueMessageType> & {
    // 当前语言唯一标识
    local: string,
    // 嵌套配置示例 TODO 删除嵌套配置示例
    name: string,
    common: {
        action: {
            getSoftware: string,
            getUserProfile: string,
            setUserProfile: string,
            uploadFile: string,
            videoQuery: string,
        },
        hide: string,
        level: {
            b: string,
            i: string,
            e: string,
        },
        mode: {
            std: string,
            nf: string,
            ng: string,
            dg: string,
        }
        msg: {
            actionFail: string,
            actionSuccess: string,
            agreeTAC: string,
            confirmPasswordFail: string,
            connectionFail: string,
            emailCodeSent: string,
            emptyEmail: string,
            emptyEmailCode: string,
            emptyPassword: string,
            emptyUsername: string,
            fileTooLarge: string,
            invalidEmail: string,
            invalidEmailCode: string,
            invalidPassword: string,
            invalidUsername: string,
            logoutFail: string,
            logoutSuccess: string,
            realNameRequired: string,
        },
        prop: {
            action: string,
            designator: string,
            fileName: string,
            is: string,
            op: string,
            level: string,
            realName: string,
            sex: string,
            status: string,
            time: string,
            timems: string,
            upload_time: string,
        }
        response: {
            OK: '',
            BadRequest: string,
            Forbidden: string,
            InternalServerError: string,
            NotFound: string,
            PayloadTooLarge: string,
            TooManyRequests: string,
            UnsupportedMediaType: string,
        },
        show: string,
        toDo: string,
    },
    forgetPassword: {
        title: string,
        email: string,
        captcha: string,
        getEmailCode: string,
        emailCode: string,
        password: string,
        confirmPassword: string,
        confirm: string,
        success: string,
    },
    login: {
        title: string,
        username: string,
        password: string,
        captcha: string,
        forgetPassword: string,
        keepMeLoggedIn: string,
        confirm: string
    },
    menu: {
        ranking: string,
        video: string,
        world: string,
        guide: string,
        score: string,
        profile: string,
        welcome: string,
        login: string,
        logout: string,
        register: string,
        setting: string,
        downloads: string,
        links: string,
        team: string
    },
    profile: {
        changeAvatar: string,
        realname: string,
        realnameInput: string,
        signature: string,
        signatureInput: string,
        change: string,
        confirmChange: string,
        cancelChange: string,
        designator: string,
        msg: {
            avatarChange: string,
            avatarFormat: string,
            avatarFilesize: string,
            realnameChange: string,
            signatureChange: string,
        },
        records: {
            title: string,
            modeRecord: string
        }
        videos: string,
        upload: {
            title: string,
            dragOrClick: string,
            uploadAll: string,
            cancelAll: string,
            constraintNote: string,
            error: {
                collision: string,
                custom: string,
                designator: string,
                fail: string,
                fileext: string,
                filename: string,
                filesize: string,
                pass: string,
                process: string,
                upload: string,
            }
        }
    },
    register: {
        title: string,
        username: string,
        email: string,
        captcha: string,
        getEmailCode: string,
        emailCode: string,
        password: string,
        confirmPassword: string,
        agreeTo: string,
        termsAndConditions: string,
        confirm: string,
    },
    setting: {
        appearance: string,
        darkMode: string,
        languageSwitch: string,
        menuFontSize: string,
        menuHeight: string,
        menuLayout: string,
        menuLayoutAbstract: string,
        menuLayoutDefault: string,
    },
}
