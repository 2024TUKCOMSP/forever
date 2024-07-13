package com.planetcopapplication.forever

import android.content.ContentValues.TAG
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.Toast
import androidx.activity.enableEdgeToEdge
import androidx.activity.result.ActivityResultLauncher
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContentProviderCompat.requireContext
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.google.android.gms.auth.api.signin.GoogleSignIn
import com.google.android.gms.auth.api.signin.GoogleSignInAccount
import com.google.android.gms.auth.api.signin.GoogleSignInClient
import com.google.android.gms.auth.api.signin.GoogleSignInOptions
import com.google.android.gms.common.api.ApiException
import com.google.android.gms.common.api.Scope
import com.google.android.material.snackbar.Snackbar
import com.google.firebase.Firebase
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.GoogleAuthProvider
import com.google.firebase.auth.auth
import com.planetcopapplication.forever.databinding.ActivityStartLoginBinding
import java.security.AccessController.getContext

//https://firebase.google.com/docs/auth/android/google-signin?hl=ko

const private  val RC_SIGN_IN = 300
class StartLoginActivity : AppCompatActivity() {
    companion object {
        private val TAG = StartLoginActivity::class.java.getSimpleName();
    }

    private lateinit var binding:ActivityStartLoginBinding

    //private lateinit var client: GoogleSignInClient
    private val REQ_ONE_TAP = 2  // Can be any integer unique to the Activity
    private var showOneTapUI = true
    //구글 로그인 위해 추가한 코드
    //https://jamie-dev.tistory.com/128

    // See: https://developer.android.com/training/basics/intents/result
    private lateinit var auth: FirebaseAuth
    private lateinit var mGoogleSignInClient: GoogleSignInClient
    private lateinit var startGoogleLoginForResult : ActivityResultLauncher<Intent>
    private lateinit var mGoogleSignInOptions: GoogleSignInOptions
    //출처: https://faith-developer.tistory.com/183 [개발 이야기:티스토리]

    /*
    private val googleAuthLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()){
        val task = GoogleSignIn.getSignedInAccountFromIntent(data)

        try{
            val account = task.getResult(ApiException::class.java)
            account.idToken?.let{
                // 클라단에서 바로 이름, 이메일 등이 필요하다면 아래와 같이 account를 통해 각 메소드를 불러올 수 있다.
                val userName = account.givenName
                val serverAuth = account.serverAuthCode

                moveSignUpActivity()
            } //서버에서 idToken 보내기
        }catch (e: ApiException) {
            Log.e(StartLoginActivity::class.java.simpleName, e.stackTraceToString())
        }

    }*/
    //https://velog.io/@akimcse/Android-Google-Login-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-with-Kotlin

    //Google 로그인을 위해 GoogleSignInClient 객체 제작, GoogleSignInOptions 넘겨줌
    private fun getGoogleClient(): GoogleSignInClient {
        val googleSignInOption = GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN)
            .requestScopes(Scope("https://www.googleapis.com/auth/pubsub"))
            //.requestServerAuthCode(getString(R.string.google_login_client_id)) // string 파일에 저장해둔 client id 를 이용해 server authcode를 요청한다.
            .requestEmail() // 이메일도 요청할 수 있다.
            .build()

        return GoogleSignIn.getClient(StartLoginActivity(), googleSignInOption)
    }

    private fun firebaseAuthWithGoogle(acct: GoogleSignInAccount) {
        Log.d(TAG, "firebaseAuthWithGoogle:" + acct.id!!)

        val credential = GoogleAuthProvider.getCredential(acct.idToken, null)
        auth.signInWithCredential(credential)
            .addOnCompleteListener(this) { task ->
                if (task.isSuccessful) {
                    // Sign in success, update UI with the signed-in user's information
                    Log.d(TAG, "signInWithCredential:success")
                    val user = auth.currentUser
                    //updateUI(user)
                } else {
                    // If sign in fails, display a message to the user.
                    Log.w(TAG, "signInWithCredential:failure", task.exception)
                    //Snackbar.make(main_layout, "Authentication Failed.", Snackbar.LENGTH_SHORT).show()
                    //updateUI(null)
                }

                // ...
            }
    }
    //출처: https://faith-developer.tistory.com/183 [개발 이야기:티스토리]


/*
    private fun requestGoogleLogin() {
        mGoogleSignInClient.signOut()
        val signInIntent = mGoogleSignInClient.signInIntent
        googleAuthLauncher.launch(signInIntent)
    }
*/
    private fun moveSignUpActivity() {
        this.run {
            startActivity(Intent(this, StartLoginActivity::class.java))
            finish()
        }
    }


    /**
     * GoogleSignInAccount 객체에서 ID 토큰을 가져와서 Firebase 사용자 인증 정보로 교환하고 Firebase 사용자 인증 정보를 사용해 인증.
     */




    /**
     * ##########################
     *  Override Method
     * ##########################
     */

    //활동을 초기화할 때 사용자가 현재 로그인되어 있는지 확인합니다
    public override fun onStart() {
        super.onStart()
        // Check if user is signed in (non-null) and update UI accordingly.
        val currentUser = auth.currentUser
        if (currentUser != null) {
            //reload()
            currentUser.reload()
            //로그인 되어있을 시 리로드?
        }
        //Check if user is signed in (non-null) and update UI accordingly.
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        binding = ActivityStartLoginBinding.inflate(layoutInflater)
        setContentView(binding.root)
        //setContentView(R.layout.activity_start_login)

        // Initialize Firebase Auth
        auth = Firebase.auth

        val googleSignInOption = GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN)

        var user = Firebase.auth.currentUser
        user?.let{
            //Name, email address, and profile photo Url
            val name = it.displayName
            val email = it. email
            val photoUrl = it.photoUrl

            //check if User's email is verified
            val emailVerified = it.isEmailVerified

            // The user's ID, unique to the Firebase project. Do NOT use this value to
            // authenticate with your backend server, if you have one. Use
            // FirebaseUser.getIdToken() instead.
            val uid = it.uid
        }
        //구글
        mGoogleSignInOptions = GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN)
            //.requestIdToken(getString(R.string.google_default_web_client_id))
            .requestEmail()
            .build()
        mGoogleSignInClient = GoogleSignIn.getClient(this, mGoogleSignInOptions)
        auth = FirebaseAuth.getInstance()

        //initOnClickListener()






        /*
        버튼 관련 프로세스
         */

        var googleLoginBtn = findViewById<Button>(R.id.googleLoginBtn)
        googleLoginBtn.setOnClickListener {
            requestGoogleLogin()
        }

        var mainActivityBtn = findViewById<Button>(R.id.appleLoginBtn)
        mainActivityBtn.setOnClickListener{
            var intent = Intent(applicationContext, MainActivity::class.java)
            startActivity(intent)
        }//메인 퀵스루 버튼

    }

    private fun signIn() {
        mGoogleSignInClient.signOut()
        val signInIntent = mGoogleSignInClient.signInIntent
        startActivityForResult(signInIntent, RC_SIGN_IN)
    }

    fun successLogin(){
        startActivity(Intent(this, MainActivity::class.java))
        finish()
    }
    //출처: https://faith-developer.tistory.com/183 [개발 이야기:티스토리]

    public override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        // Result returned from launching the Intent from GoogleSignInApi.getSignInIntent(...);
        if (requestCode == RC_SIGN_IN) {
            val task = GoogleSignIn.getSignedInAccountFromIntent(data)
            try {
                // Google Sign In was successful, authenticate with Firebase
                val account = task.getResult(ApiException::class.java)
                firebaseAuthWithGoogle(account!!)
            } catch (e: ApiException) {
                // Google Sign In failed, update UI appropriately
                Log.w(TAG, "Google sign in failed", e)
                // ...
            }
        }
    }





}